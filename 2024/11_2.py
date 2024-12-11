# Advent of Code 2024: Day 11
from aoc import get_data
from tqdm import tqdm
from functools import cache
from collections import Counter
data = get_data(11, splitlines=False)

@cache
def new_stone_s(stone_num: int | list[int]):
    if isinstance(stone_num, list):
        return [new_stone_s(x) for x in stone_num]
    if stone_num == 0:
        return 1
    stone_str = str(stone_num)
    stone_str_len = len(stone_str)
    if stone_str_len %2 == 0:
        lhs, rhs = stone_str[:stone_str_len//2], stone_str[stone_str_len//2:]
        return [int(lhs), int(rhs)]
    return stone_num * 2024

stones_after_15_moves = {} #stone_num: Counter of resulting stones

stones = Counter(int(x) for x in data.split())
total_updates = 75

for i in range(0, total_updates, 15):
    new_stones = Counter()
    for stone, count in tqdm(stones.items()):
        if stone in stones_after_15_moves:
            # use cached result
            for resulting_stone, resulting_count in stones_after_15_moves[stone].items():
                new_stones[resulting_stone] += resulting_count * count
        else:
            # "simulate" 15 moves
            current_stones = Counter({stone: 1})
            for j in range(15):
                next_stones = Counter()
                for s, s_count in current_stones.items():
                    t = new_stone_s(s)
                    if isinstance(t, list):
                        for new_s in t:
                            next_stones[new_s] += s_count
                    else:
                        next_stones[t] += s_count
                current_stones = next_stones
            
            # add current num to cache
            stones_after_15_moves[stone] = current_stones
            for resulting_stone, resulting_count in current_stones.items():
                new_stones[resulting_stone] += resulting_count * count

    stones = new_stones
    print(i, sum(stones.values()))

print("Final length:", sum(stones.values()))
