from gate import qc

from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator

tests = [
    ("CCX target=q0", lambda c: c.ccx(1,2,0)),
    ("CCX target=q1", lambda c: c.ccx(0,2,1)),
    ("CCX target=q2", lambda c: c.ccx(0,1,2)),
]

for name, build in tests:
    ref = QuantumCircuit(3)
    build(ref)
    print(name, Operator(qc).equiv(Operator(ref)))