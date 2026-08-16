from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

q0 = 0      # control
q1 = 1      # control
q2 = 2      # target

qc.ry(-3.141592653589793/4, q2)

qc.cx(q0, q2)

qc.ry(-3.141592653589793/4, q2)

qc.cx(q1, q2)

qc.ry(3.141592653589793/4, q2)

qc.cx(q0, q2)

qc.ry(3.141592653589793/4, q2)

print(qc)