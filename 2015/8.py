# Advent of Code 2015: Day 8
# @Author: Linus Horn

from aoc import get_data
data = get_data(8, splitlines=True)


# Part 1
# cound the difference between the length of the string and the length of the string without the escape characters
def part1(data):
    return sum(len(line) - len(eval(line)) for line in data)

print(part1(data))


# Part 2
# encode each code representation as a new string (add escape characters \ and ")

def part2(data):
    return sum(2 + line.count('"') + line.count('\\') for line in data)

print(part2(data))