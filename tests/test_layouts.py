# from qiskit.transpiler import CouplingMap
# from layouts import generate_layouts

# coupling_map = CouplingMap.from_heavy_hex(3)

# for k in [3, 4, 7]:
#     layouts = generate_layouts(coupling_map, k)
#     print(f"{k} qubits : {len(layouts)} layouts")


# import math

# for k in [3,4,7]:
#     layouts = generate_layouts(coupling_map, k)
#     print(k, len(layouts)*math.factorial(k))


# from qiskit.transpiler import CouplingMap

# coupling_map = CouplingMap.from_heavy_hex(3)

# print(coupling_map.physical_qubits)
# print(len(coupling_map.physical_qubits))


from itertools import combinations
from collections import deque
from qiskit.transpiler import CouplingMap

coupling_map = CouplingMap.from_heavy_hex(3)

graph = {q: set() for q in coupling_map.physical_qubits}

for u, v in coupling_map.get_edges():
    graph[u].add(v)
    graph[v].add(u)


def connected(nodes):
    nodes = set(nodes)

    start = next(iter(nodes))
    q = deque([start])
    visited = set()

    while q:
        u = q.popleft()

        if u in visited:
            continue

        visited.add(u)

        for v in graph[u]:
            if v in nodes and v not in visited:
                q.append(v)

    return visited == nodes


for k in [3, 4, 7]:
    cnt = 0

    for subset in combinations(graph.keys(), k):
        if connected(subset):
            cnt += 1

    print(k, cnt)