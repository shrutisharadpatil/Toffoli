from qiskit.quantum_info import Operator
from qiskit.circuit.library import CCXGate
from gate import qc

print("="*60)
print("Candidate D5")
print("="*60)

print(qc)

print("\nEquivalent to CCX:")
print(Operator(qc).equiv(Operator(CCXGate())))

print("\nGate counts:")
print(qc.count_ops())

print("\nCircuit depth:")
print(qc.depth())