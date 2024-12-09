# Advent of Code 2024: Day 9
from aoc import get_data
from tqdm import tqdm
data = get_data(9, splitlines=False)

#data = "2333133121414131402"

ids = []
filesystem = []
n_free_space = 0
for idx, char in enumerate(data):
    num = int(char)
    if idx % 2 == 0:
        filesystem.extend([idx//2] * num)
        ids.append(idx//2)
    else:
        # -1 means free space
        filesystem.extend([-1] * num)
        n_free_space += num

def get_free_space(fs: list, size: int) -> int:
    # get the index of the first free space of size `size`
    for idx, elem in enumerate(fs):
        if elem == -1:
            if fs[idx:idx+size] == [-1] * size:
                return idx
    return -1


for id in tqdm(reversed(ids), total=len(ids)):
    idx = filesystem.index(id)
    size = filesystem.count(id)
    free_space_idx = get_free_space(filesystem, size)

    if idx < free_space_idx or free_space_idx == -1:
        continue

    # swap
    filesystem[free_space_idx:free_space_idx+size] = filesystem[idx:idx+size]
    filesystem[idx:idx+size] = [-1] * size



checksum = 0
for idx, elem in enumerate(filesystem):
    if elem == -1:
        continue
    checksum += idx * elem

print(checksum)
