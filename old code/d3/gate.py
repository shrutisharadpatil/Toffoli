from qiskit import QuantumCircuit

qc = QuantumCircuit(3)

# Initial layer
qc.tdg(0)
qc.tdg(1)
qc.h(2)

# CX 1
qc.cx(2,0)

# T
qc.t(0)

# CX 2
qc.cx(1,2)

# T
qc.t(2)

# CX 3
qc.cx(1,0)

# Tdg
qc.tdg(0)

# CX 4
qc.cx(1,2)

# CX 5
qc.cx(2,0)

# T
qc.t(0)

# CX 6  <-- this was missing
qc.cx(1,0)

# Final
qc.tdg(2)
qc.h(2)

print(qc.draw())