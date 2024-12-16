# Advent of Code 2024: Day 14
from aoc import get_data
import re
import matplotlib.pyplot as plt
from tqdm import tqdm
data = get_data(14, splitlines=True)

num_re = re.compile(r"-?\d+")

t = 0
width, height = 101, 103
board = [[0 for _ in range(width)] for _ in range(height)]


robots = []
for line in data:
    nums = num_re.findall(line)
    pos = tuple(map(int, nums[:2]))
    vel = tuple(map(int, nums[2:]))
    #print(pos, vel)
    robots.append((pos, vel))
    board[pos[1]][pos[0]] = board[pos[1]][pos[0]] + 1


def simulate_robots(robots, t):
    # clear board of robots
    for y in range(height):
        for x in range(width):
            board[y][x] = 0

    for pos, vel in robots:
        x, y = pos
        x += vel[0] * t
        y += vel[1] * t
        if 0 <= x < width and 0 <= y < height:
            # robots can stack on top of each other
            # so we need to keep track of how many robots are at each position
            board[y][x] = board[y][x] + 1
        else:
            # wrap around
            x = x % width
            y = y % height
            board[y][x] = board[y][x] + 1

def print_field():
    for y in range(height):
        for x in range(width):
            val = board[y][x]
            print("." if val == 0 else "#", end="")
        print()

print_field()
print()

for t in range(101):
    simulate_robots(robots, t)


mid_x = width // 2
mid_y = height // 2

quadrants_n_robots = [0,0,0,0]
for y in range(height):
    print()
    for x in range(width):
        if x == mid_x or y == mid_y:
            continue
        if board[y][x] > 0:
            if x < mid_x and y < mid_y:
                quadrants_n_robots[0] += board[y][x]
            elif x >= mid_x and y < mid_y:
                quadrants_n_robots[1] += board[y][x]
            elif x < mid_x and y >= mid_y:
                quadrants_n_robots[2] += board[y][x]
            else:
                quadrants_n_robots[3] += board[y][x]

#print_field()

print(quadrants_n_robots)
print(quadrants_n_robots[0] * quadrants_n_robots[1] * quadrants_n_robots[2] * quadrants_n_robots[3])

fields_to_check = []
dist = 20
for y in range(height):
    for x in range(width):
        if (y-mid_y)**2 + (x-mid_x)**2 < dist**2:
            fields_to_check.append((x, y))

for t in tqdm(range(1, 20_000)):
    simulate_robots(robots, t)
    n_robots = 0
    for field in fields_to_check:
        n_robots += board[field[1]][field[0]]
    if n_robots > 175:
        print(t)
        print_field()
        break

    