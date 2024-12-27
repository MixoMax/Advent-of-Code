# Advent of Code 2024: Day 18
from aoc import get_data, printd, set_debug, get_debug, nums
from collections import deque
from tqdm import tqdm

set_debug(True)
data = get_data(18, splitlines=True, year_num=2024)

width, height = 71, 71

grid = [["." for _ in range(width)] for _ in range(height)]

def print_grid(grid):
    for row in grid:
        print("".join(row))


for idx, row in enumerate(data):
    if idx == 1024:
        break
    x, y = nums(row)
    grid[y][x] = "#"



start_pos = (0, 0)
end_pos = (height - 1, width - 1)

grid[start_pos[0]][start_pos[1]] = "S"
grid[end_pos[0]][end_pos[1]] = "E"

print_grid(grid)

def bfs(grid, start, end):
    queue = deque([(start, 0)])  # (position, distance)
    visited = {start}
    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) == end:
            return dist
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < height and 0 <= ny < width and grid[nx][ny] != "#" and (nx, ny) not in visited:
                queue.append(((nx, ny), dist + 1))
                visited.add((nx, ny))
    return -1  # No path found


shortest_path_length = bfs(grid, start_pos, end_pos)
print(f"Shortest path length: {shortest_path_length}")

for idx, row in tqdm(enumerate(data)):
    if idx < 1024:
        continue
    x, y = nums(row)
    grid[y][x] = "#"

    if bfs(grid, start_pos, end_pos) == -1:
        print("First Byte to cut of Access to the End: ", x,y)
        break