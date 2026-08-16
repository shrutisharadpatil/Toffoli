from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import RCCXGate

# -------------------------------------------------
# Original circuit
# -------------------------------------------------

qc = QuantumCircuit(3)
qc.append(RCCXGate(), [0, 1, 2])

print("=" * 60)
print("Original circuit")
print("=" * 60)

print(qc)

# -------------------------------------------------
# Decompose
# -------------------------------------------------

decomp = qc.decompose()

print("\n")
print("=" * 60)
print("Decomposition")
print("=" * 60)

print(decomp)

print("\nGate counts:")
print(decomp.count_ops())

print("\nCircuit depth:")
print(decomp.depth())

# -------------------------------------------------
# Transpile to Heron basis
# -------------------------------------------------

basis = ["cz", "rz", "sx"]

trans = transpile(
    decomp,
    basis_gates=basis,
    optimization_level=3,
)

print("\n")
print("=" * 60)
print("Transpiled circuit")
print("=" * 60)

print(trans)

print("\nGate counts:")
print(trans.count_ops())

print("\nCircuit depth:")
print(trans.depth())

print("\nBasis gates used:")
print(trans.count_ops().keys())

print("\nNative gate sequence:")

for inst in trans.data:
    gate = inst.operation.name
    qubits = [f"q{trans.find_bit(q).index}" for q in inst.qubits]
    print(f"{gate:4} {' '.join(qubits)}")