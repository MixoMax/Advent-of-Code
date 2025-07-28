# Advent of Code 2024: Day 6
from aoc import get_data
from tqdm import tqdm
data = get_data(6, splitlines=True)

y_max = len(data)
x_max = len(data[0])

# find initial guard position
for y, row in enumerate(data):
    for x, cell in enumerate(row):
        if cell not in [".", "#"]:
            guard = (x, y)
            match cell:
                case "^": direction = "up"
                case "v": direction = "down"
                case "<": direction = "left"
                case ">": direction = "right"
            break

og_guard = guard
og_direction = direction


def next_move(x, y, direction):
    match direction:
        case "up":    return (x, y - 1)
        case "down":  return (x, y + 1)
        case "left":  return (x - 1, y)
        case "right": return (x + 1, y)


# part 1:
# guard moves until it hits a wall (#)
# count how many distinct cells it visited

visited = set()
while True:
    visited.add(guard)
    x, y = guard
    next_x, next_y = next_move(x, y, direction)
    
    # check if next move is out of bounds
    if not (0 <= next_x < x_max and 0 <= next_y < y_max):
        break

    # check if next move is a wall
    if data[next_y][next_x] == "#":
        match direction:
            case "up":    direction = "right"
            case "down":  direction = "left"
            case "left":  direction = "up"
            case "right": direction = "down"
        continue

    guard = (next_x, next_y)

print(len(visited))


# part 2:

# Count the number of positions we can place an obstacle in to make the guard go into an infinite loop

def is_wall(x, y, board):
    return board[y][x] == "#"

def get_next_move(x,y,direction, board):
    next_x, next_y = next_move(x, y, direction)
    if not (0 <= next_x < x_max and 0 <= next_y < y_max):
        return None
    if is_wall(next_x, next_y, board):
        match direction:
            case "up":    direction = "right"
            case "down":  direction = "left"
            case "left":  direction = "up"
            case "right": direction = "down"

        return (x,y, direction)
    return (next_x, next_y, direction)

def is_infinite_loop(x, y, direction, board):
    visited = set()
    while True:
        visited.add((x,y,direction))
        next_move = get_next_move(x, y, direction, board)
        if not next_move:
            # out of bounds
            return False
        x, y, direction = next_move
        if (x,y,direction) in visited:
            return True

count = 0
for y, row in tqdm(enumerate(data), total=y_max):
    for x, cell in enumerate(row):
        if cell == ".":
            board = data.copy()
            board[y] = board[y][:x] + "#" + board[y][x+1:]

            if is_infinite_loop(og_guard[0], og_guard[1], og_direction, board):
                count += 1

print(count)