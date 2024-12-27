# Advent of Code 2024: Day 23
from aoc import get_data, set_debug
import itertools
from multiprocessing import Pool, cpu_count
from typing import List, Optional
set_debug(True)
data: list[str] = get_data(23, splitlines=True, year_num=2024)

connections: dict[str, list[str]] = {}
for line in data:
    a, b = line.split('-')
    connections.setdefault(a, []).append(b)
    connections.setdefault(b, []).append(a)

interconnected_sets = []
for a in connections:
    for b in connections[a]:
        if b > a: # Avoid duplicates and self-connections
            for c in connections[a]:
                if c > b and c in connections[b]:
                    interconnected_sets.append(sorted([a, b, c]))

interconnected_sets = list(set(tuple(s) for s in interconnected_sets)) #remove duplicates
count = 0
for s in interconnected_sets:
    if any(node.startswith('t') for node in s):
        count += 1

print("Part 1:", count)

# Part 2
# Find the largest set of computers that are all connected to each other

def is_fully_connected(computers: list[str]) -> bool:
    # Check if all computers are connected to each other
    for a in computers:
        for b in computers:
            if a != b and b not in connections[a]:
                return False
    return True

def check_combinations_batch(size_and_start: tuple[int, int]) -> Optional[List[str]]:
    size, start = size_and_start
    chunk_size = 1000
    for i in range(start, start + chunk_size):
        try:
            combo = list(itertools.islice(itertools.combinations(connections, size), i, i + 1))[0]
            if is_fully_connected(combo):
                return combo
        except IndexError:
            return None
    return None

with Pool(cpu_count()) as pool:
    for size in range(len(connections), 0, -1):
        batch_starts = [(size, i) for i in range(0, len(connections) ** 2, 1000)]
        
        for result in pool.imap_unordered(check_combinations_batch, batch_starts):
            if result:
                print("Part 2:", ",".join(sorted(result)))
                with open("23_result.txt", "w") as f:
                    f.write(",".join(sorted(result)))
                pool.terminate()
                quit()