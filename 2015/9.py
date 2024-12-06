# Advent of Code 2015: Day 9
# @Author: Linus Horn

from aoc import get_data
data = get_data(9, splitlines=True)

from itertools import permutations

# Part 1
# find the shortest path that visits all cities exactly once

cities = set()
distances = {}
for line in data:
    start, _, end, _, distance = line.split()
    cities.add(start)
    cities.add(end)
    distances[(start, end)] = int(distance)
    distances[(end, start)] = int(distance)

def shortest_path(cities, distances):
    return min(sum(distances[(cities[i], cities[i+1])] for i in range(len(cities) - 1)) for cities in permutations(cities))

print(shortest_path(cities, distances))


# Part 2

def longest_path(cities, distances):
    return max(sum(distances[(cities[i], cities[i+1])] for i in range(len(cities) - 1)) for cities in permutations(cities))

print(longest_path(cities, distances))