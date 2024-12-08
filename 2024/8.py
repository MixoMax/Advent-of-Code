# Advent of Code 2024: Day 8
from aoc import get_data
data = get_data(8, splitlines=True)


antennas = {}
for y in range(len(data)):
    for x in range(len(data[0])):
        char = data[y][x]
        if char == ".":
            continue
        if char not in antennas:
            antennas[char] = []
        antennas[char].append((x, y))



all_coords = []
all_coords_p2 = []
for name, coords in antennas.items():
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i == j:
                continue
            c1 = coords[i]
            c2 = coords[j]

            c1_to_c2 = (c2[0] - c1[0], c2[1] - c1[1])
            c3 = (c1[0] + 2*c1_to_c2[0], c1[1] + 2*c1_to_c2[1])
            if (c3[0] >= 0 and c3[0] < len(data[0]) and c3[1] >= 0 and c3[1] < len(data)):
                all_coords.append(c3)


            for n in range(1, 100):
                c3 = (c1[0] + n*c1_to_c2[0], c1[1] + n*c1_to_c2[1])
                if (c3[0] >= 0 and c3[0] < len(data[0]) and c3[1] >= 0 and c3[1] < len(data)):
                    all_coords_p2.append(c3)
                else:
                    break
            
            for n in range(1, -100, -1):
                c3 = (c1[0] + n*c1_to_c2[0], c1[1] + n*c1_to_c2[1])
                if (c3[0] >= 0 and c3[0] < len(data[0]) and c3[1] >= 0 and c3[1] < len(data)):
                    all_coords_p2.append(c3)
                else:
                    break

all_coords = list(set(all_coords))
all_coords_p2 = list(set(all_coords_p2))

print(len(all_coords))
print(len(all_coords_p2))