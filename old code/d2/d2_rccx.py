from qiskit import QuantumCircuit
from qiskit.circuit.library import RCCXGate

qc = QuantumCircuit(3)
qc.append(RCCXGate(), [0, 1, 2])

print("===== Relative-Phase Toffoli (RCCX) =====")
print(qc)