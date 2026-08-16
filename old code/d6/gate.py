from qiskit import QuantumCircuit

qc = QuantumCircuit(7)

# data qubits
x = 0
y = 1
z = 2

# ancillas
a1 = 3
a2 = 4
a3 = 5
a4 = 6

qc.h(z)
# -------------------------------------------------
# Stage 1 : Compute ancillas
# -------------------------------------------------

qc.cx(y, a3)

qc.cx(x, a1)

qc.cx(y, a2)

qc.cx(z, a3)

qc.cx(a1, a4)

qc.cx(x, a2)

qc.cx(z, a4)

qc.cx(a3, a1)

# -------------------------------------------------
# T layer
# -------------------------------------------------

qc.t(x)
qc.t(y)
qc.t(z)

qc.t(a1)

qc.tdg(a2)
qc.tdg(a3)
qc.tdg(a4)

# -------------------------------------------------
# Stage 3 : Uncompute
# -------------------------------------------------

qc.cx(a3, a1)

qc.cx(z, a4)

qc.cx(x, a2)

qc.cx(a1, a4)

qc.cx(z, a3)

qc.cx(y, a2)

qc.cx(x, a1)

qc.cx(y, a3)

qc.h(z)
print(qc)