# Advent of Code 2015: Day 1
# @Author: Linus Horn

with open("./data/1.txt") as f:
    data = f.read()

# Part 1
floor = data.count("(") - data.count(")")
print(floor)


# Part 2
floor = 0
for idx, char in enumerate(data):
    if char == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(idx + 1)
        break