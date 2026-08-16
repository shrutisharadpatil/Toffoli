from gate import qc

print("=" * 60)
print("Candidate D8")
print("=" * 60)

print(qc)

print("\nGate counts:")
print(qc.count_ops())

print("\nCircuit depth:")
print(qc.depth())

print("\nLogical qubits:")
print("4 (3 data qubits + 1 ancilla)")

print("\nAncillas:")
print("1 clean ancilla")

print("\nVerification:")
print("Not compared against CCX.")
print("Implements the intermediate Toffoli* construction described by Jones.")
print("This circuit differs from an exact Toffoli by an additional controlled-S† operation.")