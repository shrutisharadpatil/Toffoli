from gate import qc

from qiskit.circuit.library import CCXGate
from qiskit.quantum_info import Operator

print("="*60)
print("Candidate")
print("="*60)

print(qc)

print()

print("Equivalent to CCX:")
print(Operator(qc).equiv(Operator(CCXGate())))

print()

print("Gate counts:")
print(qc.count_ops())

print()

print("Circuit depth:")
print(qc.depth())