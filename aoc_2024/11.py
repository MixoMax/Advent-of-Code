# Advent of Code 2024: Day 11
from aoc import get_data
from tqdm import tqdm
from functools import cache
data = get_data(11, splitlines=False)

@cache
def new_stone_s(stone_num: int):
    if stone_num == 0:
        return 1
    stone_str = str(stone_num)
    stone_str_len = len(stone_str)
    if stone_str_len %2 == 0:
        lhs, rhs = stone_str[:stone_str_len//2], stone_str[stone_str_len//2:]
        return [int(lhs), int(rhs)]
    return stone_num * 2024

stones = [int(x) for x in data.split()]
n_updates = 25
for i in range(n_updates):
    new_stones = [new_stone_s(x) for x in stones ]
    stones = []
    for stone in new_stones:
        if isinstance(stone, list):
            stones.extend(stone)
        else:
            stones.append(stone)

    print(i, len(stones))

print("Final length:", len(stones))

