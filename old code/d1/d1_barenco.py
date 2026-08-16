from qiskit import QuantumCircuit

# Create circuit
qc = QuantumCircuit(3)

# Add Toffoli
qc.ccx(0, 1, 2)

print("===== Original Circuit =====")
print(qc.draw())

# Decompose once
d1 = qc.decompose()

print("\n===== After One Decomposition =====")
print(d1.draw())

print("\nGate Counts:")
print(d1.count_ops())

print("\nCircuit Depth:")
print(d1.depth())