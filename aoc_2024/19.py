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
def is_possible(available_combinations: tuple[str], towel_to_produce: str) -> bool:
    # from left to right, check if the towel can be produced
    # prefer longer combinations, use backtracking
    if not towel_to_produce:
        return True
    for combination in available_combinations:
        if towel_to_produce.startswith(combination):
            if is_possible(available_combinations, towel_to_produce[len(combination):]):
                return True
    return False

n_possible = 0
for towel in tqdm(to_produce):
    if is_possible(available_combinations, towel):
        n_possible += 1

print(n_possible)
