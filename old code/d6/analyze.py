from gate import qc

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

x = 0
y = 1
z = 2

for bits in range(8):

    # ------------------------
    # Selinger circuit
    # ------------------------
    test1 = QuantumCircuit(7)

    # prepare xyz
    if bits & 1:
        test1.x(x)
    if bits & 2:
        test1.x(y)
    if bits & 4:
        test1.x(z)

    # ancillas remain |0000>

    test1.compose(qc, inplace=True)

    out1 = Statevector.from_instruction(test1)

    # ------------------------
    # Ideal Toffoli
    # ------------------------
    test2 = QuantumCircuit(7)

    if bits & 1:
        test2.x(x)
    if bits & 2:
        test2.x(y)
    if bits & 4:
        test2.x(z)

    test2.ccx(x, y, z)

    out2 = Statevector.from_instruction(test2)

    print(f"{bits:03b} :", out1.equiv(out2))