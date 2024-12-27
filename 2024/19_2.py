# Advent of Code 2024: Day 19
from aoc import get_data, printd, set_debug, get_debug, nums
from tqdm import tqdm
from functools import cache
set_debug(True)
data = get_data(day_num=19, splitlines=True)

available_combinations = data[0].split(", ")
available_combinations.sort(key=len, reverse=True)
available_combinations = tuple(available_combinations)


to_produce = data[1:]
# ['brwrr', 'bggr', 'gbbr', 'rrbgbr', 'ubwu', 'bwurrg', 'brgr', 'bbrgwb']

@cache
def count_ways(available_combinations: tuple[str], towel_to_produce: str) -> int:
    if not towel_to_produce:
        return 1
    count = 0
    for combination in available_combinations:
        if towel_to_produce.startswith(combination):
            count += count_ways(available_combinations, towel_to_produce[len(combination):])
    return count

ways_to_produce = []
for towel in tqdm(to_produce):
    ways_to_produce.append(count_ways(available_combinations, towel))

print(sum(ways_to_produce))