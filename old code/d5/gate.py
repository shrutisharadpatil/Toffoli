from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

c1 = 0
c2  = 2
t = 1

#qc.cx(c2, t)
qc.h(c2)

qc.cx(t, c2)
qc.tdg(c2)

qc.cx(c1, c2)
qc.t(c2)

qc.cx(t, c2)
qc.tdg(c2)
qc.tdg(t)
qc.cx(c1, c2)

qc.cx(c1, t)


qc.t(c2)
qc.tdg(t)

qc.h(c2)


qc.cx(c1, t)
qc.s(t)
#qc.cx(c2, t)
qc.t(c1)

print(qc)