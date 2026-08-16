from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime.fake_provider import FakeTorino

# ---------------------------------------
# Build the circuit
# ---------------------------------------

qc = QuantumCircuit(3)
qc.ccx(0, 1, 2)

print("=" * 60)
print("Original circuit")
print("=" * 60)
print(qc.draw())

# ---------------------------------------
# Fake IBM Heron backend
# ---------------------------------------

backend = FakeTorino()

# ---------------------------------------
# Transpile
# ---------------------------------------

tqc = transpile(
    qc,
    backend=backend,
    optimization_level=0
)

print("\n" + "=" * 60)
print("Transpiled circuit")
print("=" * 60)
print(tqc.draw())

# ---------------------------------------
# Statistics
# ---------------------------------------

print("\nGate counts:")
print(tqc.count_ops())

print("\nCircuit depth:")
print(tqc.depth())

print("\nBasis gates used:")
print(tqc.count_ops().keys())