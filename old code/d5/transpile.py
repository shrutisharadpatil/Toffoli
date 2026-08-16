from gate import qc

from qiskit import transpile

basis = ["rz", "sx", "x", "cz"]

tqc = transpile(
    qc,
    basis_gates=basis,
    optimization_level=3
)

print("="*60)
print("Original circuit")
print("="*60)

print(qc)

print("\n")

print("="*60)
print("Transpiled circuit")
print("="*60)

print(tqc)

print("\nGate counts:")
print(tqc.count_ops())

print("\nCircuit depth:")
print(tqc.depth())

print("\nBasis gates:")
print(tqc.count_ops().keys())

print("\nNative gate sequence:")

for inst in tqc.data:
    op = inst.operation.name
    qubits = [q._index for q in inst.qubits]
    print(op, qubits)