from qiskit import QuantumCircuit, transpile

qc = QuantumCircuit(3)

qc.tdg(0)
qc.tdg(1)
qc.h(2)

qc.cx(2,0)
qc.t(0)
qc.cx(1,2)
qc.t(2)
qc.cx(1,0)
qc.tdg(0)
qc.cx(1,2)
qc.cx(2,0)
qc.t(0)
qc.cx(1,0)
qc.tdg(2)
qc.h(2)

print("="*60)
print("Original circuit")
print("="*60)
print(qc.draw())

basis = ["rz","sx","x","cz"]

tqc = transpile(
    qc,
    basis_gates=basis,
    optimization_level=3
)

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

for inst, qargs, cargs in tqc.data:
    qubits = [tqc.find_bit(q).index for q in qargs]
    print(inst.name, qubits)