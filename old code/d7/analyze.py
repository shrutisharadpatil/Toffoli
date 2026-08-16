from gate import qc

print("="*60)
print("Candidate D7")
print("="*60)

print(qc)

print("\nGate counts:")
print(qc.count_ops())

print("\nCircuit depth:")
print(qc.depth())

print("\nNote:")
print("Implements a Toffoli up to a diagonal gate (relative-phase implementation).")
print("Operator.equiv(CCX) is not expected to return True.")