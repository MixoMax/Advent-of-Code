# Advent of Code 2024: Day 3
# @Author: Linus Horn
from aoc import get_data
data = get_data(3, splitlines=False)

import re
# Part 1

#re for "mul(X,Y)" where X and Y are integers
mul = re.compile(r"mul\((\d+),(\d+)\)")

s = 0
while m := mul.search(data):
    s += int(m.group(1)) * int(m.group(2))
    data = data[:m.start()] + str(int(m.group(1)) * int(m.group(2))) + data[m.end():]
print(s)



# Part 2

# ignore anything between "don't()" and "do()"
data = get_data(3, splitlines=False)

# strip out all parts of data between "don't()" and "do()"
is_enabled = True
data_filtered = ""
for i in range(len(data)):
    if data[i:i+7] == "don't()":
        is_enabled = False
    if is_enabled:
        data_filtered += data[i]
    if data[i:i+4] == "do()":
        is_enabled = True

s = 0
while m := mul.search(data_filtered):
    s += int(m.group(1)) * int(m.group(2))
    data_filtered = data_filtered[:m.start()] + str(int(m.group(1)) * int(m.group(2))) + data_filtered[m.end():]
print(s)

