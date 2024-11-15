"""Trotter circuit generation"""

from __future__ import annotations
from collections.abc import Sequence
from collections import defaultdict
import numpy as np
import rustworkx
from qiskit.circuit import QuantumCircuit, Parameter
from qiskit.circuit.library import CXGate, CZGate, ECRGate
from qiskit.providers import Backend


def remove_qubit_couplings(
    couplings: Sequence[tuple[int, int]], qubits: Sequence[int] | None = None
) -> list[tuple[int, int]]:
    """Remove qubits from a coupling list.

    Args:
        couplings: A sequence of qubit couplings.
        qubits: Optional, the qubits to remove.

    Returns:
        The input couplings with the specified qubits removed.
    """
    if qubits is None:
        return couplings
    qubits = set(qubits)
    return [edge for edge in couplings if not qubits.intersection(edge)]


def coupling_qubits(
    *couplings: Sequence[tuple[int, int]], allowed_qubits: Sequence[int] | None = None
) -> list[int]:
    """Return a sorted list of all qubits involved in 1 or more couplings lists.

    Args:
        couplings: 1 or more coupling lists.
        allowed_qubits: Optional, the allowed qubits to include. If None all
            qubits are allowed.

    Returns:
        The intersection of all qubits in the couplings and the allowed qubits.
    """
    qubits = set()
    for edges in couplings:
        for edge in edges:
            qubits.update(edge)
    if allowed_qubits is not None:
        qubits = qubits.intersection(allowed_qubits)
    return list(qubits)


def construct_layer_couplings(backend: Backend) -> list[list[tuple[int, int]]]:
    """Separate a coupling map into disjoint 2-qubit gate layers.

    Args:
        backend: A backend to construct layer couplings for.

    Returns:
        A list of disjoint layers of directed couplings for the input coupling map.
    """
    coupling_graph = backend.coupling_map.graph.to_undirected(multigraph=False)
    edge_coloring = rustworkx.graph_bipartite_edge_color(coupling_graph)

    layers = defaultdict(list)
    for edge_idx, color in edge_coloring.items():
        layers[color].append(coupling_graph.get_edge_endpoints_by_index(edge_idx))
    layers = [sorted(layers[i]) for i in sorted(layers.keys())]

    return layers


def entangling_layer(
    gate_2q: str,
    couplings: Sequence[tuple[int, int]],
    qubits: Sequence[int] | None = None,
) -> QuantumCircuit:
    """Generating a entangling layer for the specified couplings.

    This corresonds to a Trotter layer for a ZZ Ising term with angle Pi/2.

    Args:
        gate_2q: The 2-qubit basis gate for the layer, should be "cx", "cz", or "ecr".
        couplings: A sequence of qubit couplings to add CX gates to.
        qubits: Optional, the physical qubits for the layer. Any couplings involving
            qubits not in this list will be removed. If None the range up to the largest
            qubit in the couplings will be used.

    Returns:
        The QuantumCircuit for the entangling layer.
    """
    # Get qubits and convert to set to order
    if qubits is None:
        qubits = range(1 + max(coupling_qubits(couplings)))
    qubits = set(qubits)

    # Mapping of physical qubit to virtual qubit
    qubit_mapping = {q: i for i, q in enumerate(qubits)}

    # Convert couplings to indices for virtual qubits
    indices = [
        [qubit_mapping[i] for i in edge]
        for edge in couplings
        if qubits.issuperset(edge)
    ]

    # Layer circuit on virtual qubits
    circuit = QuantumCircuit(len(qubits))

    # Get 2-qubit basis gate and pre and post rotation circuits
    gate2q = None
    pre = QuantumCircuit(2)
    post = QuantumCircuit(2)

    if gate_2q == "cx":
        gate2q = CXGate()
        # Pre-rotation
        pre.sdg(0)
        pre.z(1)
        pre.sx(1)
        pre.s(1)
        # Post-rotation
        post.sdg(1)
        post.sxdg(1)
        post.s(1)
    elif gate_2q == "ecr":
        gate2q = ECRGate()
        # Pre-rotation
        pre.z(0)
        pre.s(1)
        pre.sx(1)
        pre.s(1)
        # Post-rotation
        post.x(0)
        post.sdg(1)
        post.sxdg(1)
        post.s(1)
    elif gate_2q == "cz":
        gate2q = CZGate()
        # Identity pre-rotation
        # Post-rotation
        post.sdg([0, 1])
    else:
        raise ValueError(
            f"Invalid 2-qubit basis gate {gate_2q}, should be 'cx', 'cz', or 'ecr'"
        )

    # Add 1Q pre-rotations
    for inds in indices:
        circuit.compose(pre, qubits=inds, inplace=True)

    # Use barriers around 2-qubit basis gate to specify a layer for PEA noise learning
    circuit.barrier()
    for inds in indices:
        circuit.append(gate2q, (inds[0], inds[1]))
    circuit.barrier()

    # Add 1Q post-rotations after barrier
    for inds in indices:
        circuit.compose(post, qubits=inds, inplace=True)

    # Add physical qubits as metadata
    circuit.metadata["physical_qubits"] = tuple(qubits)

    return circuit


def trotter_circuit(
    theta: Parameter | float,
    layer_couplings: Sequence[Sequence[tuple[int, int]]],
    num_steps: int,
    gate_2q: str | None = "cx",
    backend: Backend | None = None,
    qubits: Sequence[int] | None = None,
) -> QuantumCircuit:
    """Generate a Trotter circuit for the 2D Ising

    Args:
        theta: The angle parameter for X.
        layer_couplings: A list of couplings for each entangling layer.
        num_steps: the number of Trotter steps.
        gate_2q: The 2-qubit basis gate to use in entangling layers.
            Can be "cx", "cz", "ecr", or None if a backend is provided.
        backend: A backend to get the 2-qubit basis gate from, if provided
            will override the basis_gate field.
        qubits: Optional, the allowed physical qubits to truncate the
            couplings to. If None the range up to the largest
            qubit in the couplings will be used.

    Returns:
        The Trotter circuit.
    """
    if backend is not None:
        try:
            basis_gates = backend.configuration().basis_gates
        except AttributeError:
            basis_gates = backend.basis_gates
        for gate in ["cx", "cz", "ecr"]:
            if gate in basis_gates:
                gate_2q = gate
                break

    # If no qubits, get the largest qubit from all layers and
    # sepecify the range so the same one is used for all layers.
    if qubits is None:
        qubits = range(1 + max(coupling_qubits(layer_couplings)))

    # Generate the entangling layers
    layers = [
        entangling_layer(gate_2q, couplings, qubits=qubits)
        for couplings in layer_couplings
    ]

    # Construct the circuit for a single Trotter step
    num_qubits = len(qubits)
    trotter_step = QuantumCircuit(num_qubits)
    trotter_step.rx(theta, range(num_qubits))
    for layer in layers:
        trotter_step.compose(layer, range(num_qubits), inplace=True)

    # Construct the circuit for the specified number of Trotter steps
    circuit = QuantumCircuit(num_qubits)
    for _ in range(num_steps):
        circuit.rx(theta, range(num_qubits))
        for layer in layers:
            circuit.compose(layer, range(num_qubits), inplace=True)

    circuit.metadata["physical_qubits"] = tuple(qubits)
    return circuit


def get_circuit(backend):

    layer_couplings = construct_layer_couplings(backend)
    # for i, layer in enumerate(layer_couplings):
        # print(f"Layer {i}:\n{layer}\n")
    if backend.name == 'ibm_cusco':
        bad_qubits = {7,17,39,52,50,72,78,94,92,119,111}
    if backend.name == 'ibm_strasbourg':
        bad_qubits = {5,37,67,91,98,107,126,41}
    good_qubits = list(set(range(backend.num_qubits)).difference(bad_qubits))
    # print("Physical qubits:\n", good_qubits)

    from qiskit.circuit import Parameter

    num_steps = 6
    theta = Parameter("theta")
    # theta = 0
    circuit = trotter_circuit(
        theta, layer_couplings, num_steps, qubits=good_qubits, backend=backend
    )

    num_params = 12

    # 12 parameter values for Rx between [0, pi/2].
    # Reshape to outer product broadcast with obesrvables
    parameter_values = np.linspace(0, np.pi / 2, num_params).reshape((num_params, 1))
    num_params = parameter_values.size

    from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

    pm = generate_preset_pass_manager(
        backend=backend,
        initial_layout=good_qubits,
        layout_method="trivial",
        optimization_level=1,
        seed_transpiler=10
    )

    isa_circuit = pm.run(circuit)

    from qiskit.quantum_info import SparsePauliOp

    observables = []
    num_qubits = len(good_qubits)
    for q in range(num_qubits):
        observables.append(SparsePauliOp("I" * (num_qubits - q - 1) + "Z" + "I" * q))

    isa_observables = [[obs.apply_layout(layout=isa_circuit.layout)] for obs in observables]

    pub = (isa_circuit, isa_observables, parameter_values[0])

    return pub, isa_circuit, isa_observables, parameter_values
