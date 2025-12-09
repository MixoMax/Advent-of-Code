from aoc import get_data
from itertools import combinations
from tqdm import tqdm

data_lines, data_str = get_data(8, year_num=2025)

junctions = [list(map(int, line.split(","))) for line in data_lines]

def dist(a,b):
    return sum((x1 - x2) ** 2 for x1, x2 in zip(a, b)) ** 0.5

distances = {}

for a, b in combinations(range(len(junctions)), 2):
    distances[(a,b)] = dist(junctions[a], junctions[b])

circuits: list[set[int]] = [{a} for a in range(len(junctions))]
n_connections = 1000
distance_keys_sorted = sorted(list(distances.keys()), key=lambda x: distances[x])
pairs_to_connect = distance_keys_sorted[:n_connections]

for a, b in tqdm(pairs_to_connect):    
    circuit_a_idx = None
    circuit_b_idx = None
    are_in_same_circuit = False

    for idx, circuit in enumerate(circuits):
        if a in circuit and b in circuit:
            # if a and b are already in the same circuit, skip
            are_in_same_circuit = True
            break
        if a in circuit:
            circuit_a_idx = idx
        if b in circuit:
            circuit_b_idx = idx
    if are_in_same_circuit:
        continue

    if circuit_a_idx is None and circuit_b_idx is None:
        # create new circuit
        print(f"{a},{b} -> new circuit")
        circuits.append(set([a, b]))
    
    elif circuit_a_idx is not None and circuit_b_idx is None:
        # add b to circuit a
        print(f"{a},{b} -> add {b} to circuit {circuit_a_idx}")
        circuits[circuit_a_idx].add(b)
    elif circuit_a_idx is None and circuit_b_idx is not None:
        # add a to circuit b
        print(f"{a},{b} -> add {a} to circuit {circuit_b_idx}")
        circuits[circuit_b_idx].add(a)
    else:
        # a and b both in different circuits, merge them into one circuit
        print(f"{a},{b} -> merge circuit {circuit_a_idx} and circuit {circuit_b_idx}")
        circuits[circuit_a_idx] = circuits[circuit_a_idx].union(circuits[circuit_b_idx])
        del circuits[circuit_b_idx]

sizes = sorted([len(circuit) for circuit in circuits], reverse=True)
print(sizes[0] * sizes[1] * sizes[2])


circuits: list[set[int]] = [{a} for a in range(len(junctions))]
distance_keys_sorted = sorted(list(distances.keys()), key=lambda x: distances[x])

for a, b in tqdm(distance_keys_sorted):  
    circuit_a_idx = None
    circuit_b_idx = None
    are_in_same_circuit = False

    for idx, circuit in enumerate(circuits):
        if a in circuit and b in circuit:
            # if a and b are already in the same circuit, skip
            are_in_same_circuit = True
            break
        if a in circuit:
            circuit_a_idx = idx
        if b in circuit:
            circuit_b_idx = idx
    if are_in_same_circuit:
        continue

    if circuit_a_idx is None and circuit_b_idx is None:
        # create new circuit
        print(f"{a},{b} -> new circuit")
        circuits.append(set([a, b]))
    
    elif circuit_a_idx is not None and circuit_b_idx is None:
        # add b to circuit a
        print(f"{a},{b} -> add {b} to circuit {circuit_a_idx}")
        circuits[circuit_a_idx].add(b)
    elif circuit_a_idx is None and circuit_b_idx is not None:
        # add a to circuit b
        print(f"{a},{b} -> add {a} to circuit {circuit_b_idx}")
        circuits[circuit_b_idx].add(a)
    else:
        # a and b both in different circuits, merge them into one circuit
        print(f"{a},{b} -> merge circuit {circuit_a_idx} and circuit {circuit_b_idx}")
        circuits[circuit_a_idx] = circuits[circuit_a_idx].union(circuits[circuit_b_idx])
        del circuits[circuit_b_idx]
    
    if len(circuits) == 1:
        # this is the connection that connects all junctions into a single circuit
        a_x = junctions[a][0]
        b_x = junctions[b][0]
        print(a_x * b_x)