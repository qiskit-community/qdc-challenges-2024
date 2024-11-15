from qiskit import QuantumCircuit

def circuit_ex1(paramsx,repetitions):
    qc = QuantumCircuit(14)
    for j in range(repetitions):
        # 1st "layer"
        for i in range(14):
            qc.rx(paramsx[i,0],i)
        qc.barrier()
        qc.cz(range(3),range(1,4))
        qc.cz(2,4)
        qc.cz(4,5)
        qc.cz(5,6)
        qc.cz(5,7)
        qc.cz(7,8)
        qc.cz(8,9)
        qc.cz(9,10)
        qc.cz(8,11)
        qc.cz(11,12)
        qc.cz(12,13)
        qc.barrier()
        # 2nd "layer"
        for i in range(14):
            qc.rx(paramsx[i,1],i)
        qc.barrier()
        qc.cz(0,1)
        qc.cz(1,3)
        qc.cz(3,2)
        qc.cz(3,4)
        qc.cz(4,6)
        qc.cz(6,5)
        qc.cz(6,7)
        qc.cz(7,8)
        qc.cz(8,10)
        qc.cz(10,9)
        qc.cz(8,11)
        qc.cz(11,12)
        qc.cz(12,13)
        qc.barrier()

    return qc

def circuit_ex3(params):
    qc = QuantumCircuit(8)
    qc.h(range(8))
    for j in range(2):
        qc.cz(range(0,4,2),range(1,5,2))
        qc.cz(range(1,4,2),range(2,5,2))
        qc.cz(range(4,8-1),range(5,8))
        for i in range(8):
            qc.rx(params[i,j],i)
    return qc
