# Advent of Code 2024: Day 9
from aoc import get_data
data = get_data(9, splitlines=False)

#data = "2333133121414131402"

ids = set()
filesystem = []
n_free_space = 0
for idx, char in enumerate(data):
    num = int(char)
    if idx % 2 == 0:
        filesystem.extend([idx//2] * num)
        ids.add(idx//2)
    else:
        # -1 means free space
        filesystem.extend([-1] * num)
        n_free_space += num

def is_in_order(fs: list) -> bool:
    first_free_space_idx = fs.index(-1)
    # check if all elements to the right of the first free space are -1
    if len(fs) - first_free_space_idx == n_free_space:
        return True
    return False

def get_last_not_free_idx(fs: list) -> int:
    # get the index of the last element that is not -1
    for idx, elem in enumerate(reversed(fs)):
        if elem != -1:
            return len(fs) - idx - 1
    return -1


print(len(filesystem))

n = 0
while not is_in_order(filesystem):
    #print(n, end="\r")
    n += 1
    last_not_free_idx = get_last_not_free_idx(filesystem)
    first_free_space_idx = filesystem.index(-1)
    filesystem[first_free_space_idx], filesystem[last_not_free_idx] = filesystem[last_not_free_idx], filesystem[first_free_space_idx]
    

checksum = 0
for idx, elem in enumerate(filesystem):
    if elem == -1:
        continue
    checksum += idx * elem

print(checksum)