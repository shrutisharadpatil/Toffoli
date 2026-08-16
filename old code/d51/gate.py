from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

q0 = 0
q1 = 1
q2 = 2

qc.h(q2)

qc.t(q0)
qc.t(q1)
qc.t(q2)

qc.cx(q0, q1)
qc.cx(q1, q2)
qc.cx(q0, q1)

qc.t(q2)

qc.cx(q1, q2)
qc.cx(q0, q1)

qc.tdg(q1)
qc.tdg(q2)

qc.cx(q1, q2)
qc.cx(q0, q1)

qc.tdg(q2)

qc.cx(q1, q2)

qc.h(q2)

print(qc)