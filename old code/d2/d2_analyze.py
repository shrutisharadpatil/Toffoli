from qiskit import QuantumCircuit
from qiskit.circuit.library import RCCXGate

qc = QuantumCircuit(3)
qc.append(RCCXGate(), [0, 1, 2])

print("\n===== Original Circuit =====")
print(qc)

decomp = qc.decompose()

print("\n===== Decomposition =====")
print(decomp)

print("\nGate Counts:")
print(decomp.count_ops())

print("\nCircuit Depth:")
print(decomp.depth())