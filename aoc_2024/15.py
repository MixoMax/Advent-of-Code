# Advent of Code 2024: Day 15
from aoc import get_data, printd, set_debug, get_debug
set_debug(False)
data = get_data(15, splitlines=False, year_num=2024)

warehouse_map_str, move_str = data.split("\n\n")

board = [list(line) for line in warehouse_map_str.splitlines()]
# board contains "." (empty space), "#" (wall=unmovable), "@" (robot), "O" (box=movable)

robot_pos = (
    [i for i, line in enumerate(board) if "@" in line][0],
    [line.index("@") for line in board if "@" in line][0],
)



def print_board(override=False):
    global DEBUG
    if override:
        prev_debug = get_debug()
        set_debug(True)
    for line in board:
        printd("".join(line))
    if override:
        set_debug(prev_debug)




# parsing move attempts

move_attempts = []
for char in move_str:
    match char:
        case "^": move = (-1, 0)
        case "v": move = (1, 0)
        case "<": move = (0, -1)
        case ">": move = (0, 1)
        case _: continue
    move_attempts.append(move)

def make_move(move: tuple[int, int]):
    global robot_pos, board

    # move the robot 1 in the direction of move
    # if there are one or more boxes in the way, move the box as well
    # the robot can push any number of boxes at once
    # if there is a wall or box behind the box, do not move the robot or the boxes

    relevant_cells = ["@"]
    next_pos = (robot_pos[0] + move[0], robot_pos[1] + move[1])
    while board[next_pos[0]][next_pos[1]] != "#":
        cell = board[next_pos[0]][next_pos[1]]
        relevant_cells.append(cell)
        next_pos = (next_pos[0] + move[0], next_pos[1] + move[1])
        if cell == ".":
            break
    
    if relevant_cells[-1] != ".":
        return
    
    printd("relevant_cells:", relevant_cells)
    
    # at this point, relevant_cells contains:
    # [robot, box, box, ..., empty_space]
    # we need to insert it into the board as if it were
    # [empty_space, robot, box, box, ...]
    # then we have moved the robot and the boxes

    board[robot_pos[0]][robot_pos[1]] = "."
    next_pos = (robot_pos[0] + move[0], robot_pos[1] + move[1])
    robot_pos = next_pos
    board[robot_pos[0]][robot_pos[1]] = "@"

    for i, cell in enumerate(relevant_cells[1:-1]):
        next_pos = (next_pos[0] + move[0], next_pos[1] + move[1])
        board[next_pos[0]][next_pos[1]] = cell
    



for move in move_attempts:
    match move:
        case (-1, 0): printd("^")
        case (1, 0): printd("v")
        case (0, -1): printd("<")
        case (0, 1): printd(">")
    make_move(move)
    print_board()

print_board(True)

s = 0
for y in range(len(board)):
    for x in range(len(board[0])):
        cell = board[y][x]
        if cell == "O":
            s += 100*y + x

print(s)