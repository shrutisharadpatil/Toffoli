from gate import qc

from qiskit_ibm_runtime.fake_provider import FakeTorino
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager

backend = FakeTorino()

pm = generate_preset_pass_manager(
    optimization_level=3,
    backend=backend
)

transpiled = pm.run(qc)

print("="*60)
print("Original circuit")
print("="*60)
print(qc)

print()

print("="*60)
print("Transpiled circuit")
print("="*60)
print(transpiled)

print()

print("Gate counts:")
print(transpiled.count_ops())

print()

print("Circuit depth:")
print(transpiled.depth())

print()

print("Basis gates:")
print(backend.operation_names)

print()

print("Native gate sequence:")

for inst in transpiled.data:
    print(
        inst.operation.name,
        [transpiled.find_bit(q).index for q in inst.qubits]
    )