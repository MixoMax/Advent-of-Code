from aoc import get_data
from itertools import combinations
data_lines, data_str = get_data(9, year_num=2025)


corner_candidates = []
for line in data_lines:
    x,y = map(int, line.split(","))
    corner_candidates.append((x,y))

max_rectangle_size = 0
for (x1,y1), (x2,y2) in combinations(corner_candidates, 2):
    if x1 != x2 and y1 != y2:
        rectangle_size = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        max_rectangle_size = max(max_rectangle_size, rectangle_size)
        print(f"Rectangle corners: ({x1},{y1})({x2},{y2}) with size {rectangle_size}")

print(max_rectangle_size)