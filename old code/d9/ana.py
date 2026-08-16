from gate import qc

print("="*60)
print("Candidate D9")
print("="*60)

print(qc)

print("\nGate counts:")
print(qc.count_ops())

print("\nCircuit depth:")
print(qc.depth())

print("\nNote:")
print("Expected to implement the 0AT3 Toffoli from the paper.")
print("Verify equivalence after confirming the figure wiring.")