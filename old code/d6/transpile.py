from gate import qc

from qiskit import transpile
from qiskit.transpiler import CouplingMap
from qiskit.providers.fake_provider import GenericBackendV2

print("="*60)
print("Original circuit")
print("="*60)
print(qc)
print()

backend = GenericBackendV2(
    num_qubits=7,
    basis_gates=["cz", "rz", "sx"],
    coupling_map=CouplingMap.from_line(7)
)

tqc = transpile(
    qc,
    backend=backend,
    optimization_level=3
)

print("="*60)
print("Transpiled circuit")
print("="*60)
print(tqc)
print()

print("Gate counts:")
print(tqc.count_ops())

print("\nCircuit depth:")
print(tqc.depth())

print("\nBasis gates:")
print(backend.operation_names)

print("\nNative gate sequence:")

for inst in tqc.data:
    print(
        inst.operation.name,
        [tqc.find_bit(q).index for q in inst.qubits]
    )