from qiskit import QuantumCircuit
from qiskit.circuit.library import CCXGate
from qiskit.quantum_info import Operator

qc = QuantumCircuit(3)

qc.tdg(0)
qc.tdg(1)
qc.h(2)

qc.cx(2,0)
qc.t(0)
qc.cx(1,2)
qc.t(2)
qc.cx(1,0)
qc.tdg(0)
qc.cx(1,2)
qc.cx(2,0)
qc.t(0)
qc.cx(1,0)
qc.tdg(2)
qc.h(2)

print("="*60)
print("Amy Exact Toffoli")
print("="*60)

print(qc.draw())

print("\nEquivalent to CCX:")
print(Operator(qc).equiv(Operator(CCXGate())))

print("\nGate counts:")
print(qc.count_ops())

print("\nCircuit depth:")
print(qc.depth())