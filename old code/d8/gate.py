from qiskit import QuantumCircuit

qc = QuantumCircuit(4)

# x, y = controls
# z = target
# a = ancilla

x = 0
y = 1
z = 2
a = 3

# Basis change
qc.h(z)

# -----------------------------
# Left half
# -----------------------------

# x -> ancilla
qc.cx(x, a)

# fan-out from z
qc.cx(z, y)
qc.cx(z, x)
qc.cx(z, a)

# -----------------------------
# T layer
# -----------------------------

qc.tdg(x)
qc.tdg(y)

qc.t(z)
qc.t(a)

# -----------------------------
# Right half (mirror)
# -----------------------------

qc.cx(y, a)
qc.cx(z, y)
qc.cx(z, x)

qc.cx(x, a)

# Basis change
qc.h(z)

print(qc)