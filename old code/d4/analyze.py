from gate import qc
print(qc)
from qiskit.quantum_info import Operator
from qiskit.circuit.library import CCXGate

print("Equivalent:")
print(Operator(qc).equiv(Operator(CCXGate())))



