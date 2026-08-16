from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

q0 = 0
q1 = 2      # target
q2 = 1

qc.h(q1)

qc.cx(q0, q1)
qc.tdg(q0)

qc.cx(q1, q2)
qc.t(q1)
qc.tdg(q2)

qc.cx(q0, q1)
qc.cx(q1, q2)
qc.tdg(q1)
qc.t(q2)

qc.cx(q0, q1)
qc.cx(q1, q2)
qc.t(q2)

qc.cx(q0, q1)


qc.cx(q1, q2)

qc.h(q1)
qc.tdg(q2)
print(qc)