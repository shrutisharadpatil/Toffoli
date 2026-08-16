from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import CCXGate

# ----------------------------
# Step 1
# Build the Toffoli gate
# ----------------------------

qc = QuantumCircuit(3)
qc.append(CCXGate(), [0,1,2])

print("\n===== Original circuit =====")
print(qc)

# ----------------------------
# Step 2
# Decompose it
# ----------------------------

decomp = qc.decompose()

print("\n===== Paper decomposition =====")
print(decomp)

print("\nGate counts:")
print(decomp.count_ops())

print("\nDepth:")
print(decomp.depth())


# ----------------------------
# Step 3
# Transpile to the Heron basis
# ----------------------------

basis_gates = ["cz", "rz", "sx"]

transpiled = transpile(
    decomp,
    basis_gates=basis_gates,
    optimization_level=3
)

print("\n===== Transpiled Circuit =====")
print(transpiled)

print("\n===== Gate Counts =====")
print(transpiled.count_ops())

print("\n===== Circuit Depth =====")
print(transpiled.depth())

print("\n===== Basis Gates Used =====")
print(transpiled.count_ops().keys())

print("\n===== Native Gate Sequence =====")

for inst in transpiled.data:
    print(inst.operation.name, inst.qubits)