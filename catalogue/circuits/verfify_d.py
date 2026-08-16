ref = QuantumCircuit(3)
ref.ccx(0, 1, 2)

print(
    Operator(dq).equiv(
        Operator(ref)
    )
)