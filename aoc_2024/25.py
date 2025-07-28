# Advent of Code 2024: Day 25
from aoc import get_data, printd, set_debug, get_debug, nums
set_debug(True)
data = get_data(day_num=25, splitlines=False)

pieces = data.split("\n\n")

locks = []
keys = []

for piece in pieces:
    lines = piece.split("\n")
    heights = [0 for _ in range(len(lines[0]))]
    for x in range(len(lines[0])):
        vertical_line = "".join([line[x] for line in lines])
        heights[x] = vertical_line.count("#") - 1
    if set(lines[0]) == {"#"}:
        # lock
        locks.append(heights)
    else:
        # key
        keys.append(heights)

# now, locks and keys are lists of lists of heights
# for a key to fit a lock, their heights at every x must add up to a maximum of 5
n_combinations = 0
for lock in locks:
    for key in keys:
        if all([lock[x] + key[x] <= 5 for x in range(len(lock))]):
            n_combinations += 1
print(n_combinations)