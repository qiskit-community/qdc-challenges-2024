from qiskit import QuantumCircuit
from qiskit.circuit import Parameter

def TFIMCircuit(num_qubits, trotter_steps):

    circuit = QuantumCircuit(num_qubits)

    beta = Parameter("β")
    gamma = Parameter("γ")
    
    for step in range(trotter_steps):
        
        for qubit in range(num_qubits):
            circuit.rx(beta, qubit)
        for qubit in range(0, num_qubits - 1, 2):
            circuit.rzz(gamma, qubit, qubit + 1)
        for qubit in range(1, num_qubits - 1, 2):
            circuit.rzz(gamma, qubit, qubit + 1)

    return circuit

def compute_uncompute(circuit, barrier=True, inplace=False):

    inverse = circuit.inverse()
    if not inplace:
        circuit = circuit.copy()
    if barrier:
        circuit.barrier()
    circuit.compose(inverse, inplace=True)
    
    return circuit


import time
import sys
from itertools import product

# Function to create a progress bar
def progress_bar(current, total, bar_length=40):
    progress = current / total
    block = int(bar_length * progress)
    bar = "#" * block + "-" * (bar_length - block)
    sys.stdout.write(f"\rProgress: [{bar}] {current}/{total} combinations completed.")
    sys.stdout.flush()