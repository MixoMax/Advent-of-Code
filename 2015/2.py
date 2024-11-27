# Advent of Code 2015: Day 2
# @Author: Linus Horn

from r import get_data

data = get_data(2)

lines = data.split("\n")

# Part 1
total_paper = 0
for line in lines:
    l, w, h = map(int, line.split("x"))
    sides = [l*w, w*h, h*l]
    total_paper += 2*sum(sides) + min(sides)

print(total_paper)


# Part 2
total_ribbon = 0
for line in lines:
    l, w, h = sorted(map(int, line.split("x")))
    total_ribbon += 2*l + 2*w + l*w*h

print(total_ribbon)
