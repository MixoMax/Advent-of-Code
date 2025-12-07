from aoc import get_data
data_lines, data_str = get_data(4, year_num=2025)

def is_accessible(x, y, grid):
    val = grid[y][x]
    is_paper_roll = val == "@"
    num_paper_neightbors = 0
    for neighbor in [(0, 1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]:
        nx, ny = x + neighbor[0], y + neighbor[1]
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if grid[ny][nx] == "@":
                num_paper_neightbors += 1
    return is_paper_roll and num_paper_neightbors <= 3

def get_accessible_paper_rolls(grid):
    accessible_positions = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if is_accessible(x, y, grid):
                accessible_positions.add((x, y))
    return accessible_positions

grid = [list(line) for line in data_lines]
s_1 = len(get_accessible_paper_rolls(grid))
print(s_1)

# Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?
accessible_positions_total = set()
while True:
    accessible_positions = get_accessible_paper_rolls(grid)
    if not accessible_positions:
        break
    for x, y in accessible_positions:
        grid[y][x] = "."
    accessible_positions_total.update(accessible_positions)
s_2 = len(accessible_positions_total)
print(s_2)