# Advent of Code 2024: Day 9
from aoc import get_data
from tqdm import tqdm
data = get_data(10, splitlines=True)

starting_positions = []
ending_positions = []
for idx, row in enumerate(data):
    for idx2, char in enumerate(row):
        if char == "0":
            starting_positions.append((idx, idx2))
        elif char == "9":
            ending_positions.append((idx, idx2))
    

def get_num(pos: tuple[int, int]) -> int:
    return int(data[pos[0]][pos[1]]) if 0 <= pos[0] < len(data) and 0 <= pos[1] < len(data[0]) else -1


# a valid path is a path where the value of each cell of the path is the previous value + 1
# for each cell in the grid, store which 9s are reachable from it
# if a cell is not reachable, store -1
# if a cell is a 9, store -2

# initialize the grid
grid = [[[] for _ in range(len(data[0]))] for _ in range(len(data))]
for pos in ending_positions:
    grid[pos[0]][pos[1]] = -2


for num in range(8, -1, -1):
    for pos in [(i, j) for i in range(len(data)) for j in range(len(data[0]))]:
        if get_num(pos) == num:
            neighbors = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
            for neighbor in neighbors:
                if get_num(neighbor) == num + 1:
                    if get_num(neighbor) == 9:
                        grid[pos[0]][pos[1]].append(neighbor)
                    else:
                        grid[pos[0]][pos[1]] += grid[neighbor[0]][neighbor[1]] if grid[neighbor[0]][neighbor[1]] != -1 else []
            
            if grid[pos[0]][pos[1]] == []:
                grid[pos[0]][pos[1]] = -1
            else:
                #grid[pos[0]][pos[1]] = list(set(grid[pos[0]][pos[1]]))
                pass


s = 0
for starting_pos in starting_positions:
    s += len(grid[starting_pos[0]][starting_pos[1]])
print(s)