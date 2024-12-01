# Advent of Code 2015: Day 6
# @Author: Linus Horn

from aoc import get_data

data = get_data(6)


# Part 1

lights = [[False for _ in range(1000)] for _ in range(1000)]

for line in data.split("\n"):
    p1, p2 = line.split(" through ")
    p1 = p1.replace("turn ", "turn-")
    instruction, n = p1.split(" ")

    x1, y1 = n.split(",")
    x2, y2 = p2.split(",")

    # print(f"{x1=}{y1=}{x2=}{y2=}{instruction=}")

    for x in range(int(x1), int(x2)+1):
        for y in range(int(y1), int(y2)+1):
            v = lights[x][y]
            match instruction:
                case "toggle": v = False if v else True
                case "turn-on": v = True
                case "turn-off": v = False
                case _: print(instruction)
            
            lights[x][y] = v


n_lit = 0
for row in lights:
    for v in row:
        if v:
            n_lit += 1

print(n_lit)


# part 2
lights = [[0 for _ in range(1000)] for _ in range(1000)]
for line in data.split("\n"):
    p1, p2 = line.split(" through ")
    p1 = p1.replace("turn ", "turn-")
    instruction, n = p1.split(" ")

    x1, y1 = n.split(",")
    x2, y2 = p2.split(",")

    # print(f"{x1=}{y1=}{x2=}{y2=}{instruction=}")

    for x in range(int(x1), int(x2)+1):
        for y in range(int(y1), int(y2)+1):
            v = lights[x][y]
            match instruction:
                case "toggle": v += 2
                case "turn-on": v += 1
                case "turn-off": v = max(v-1, 0)
            lights[x][y] = v

total_brightness = 0
for row in lights:
    total_brightness += sum(row)
print(total_brightness)
            