# Advent of Code 2024: Day 13
from aoc import get_data
from tqdm import tqdm
from typing import List, Tuple, Callable
data = get_data(13, splitlines=True)

DEBUG = False


def printd(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)



machines: list[list[str]] = []
current_machine = []
for line in data:
    if line == "":
        machines.append(current_machine)
        current_machine = []
    else:
        current_machine.append(line)

def lowest_tokens(prize_coords: tuple[int, int], button_a_x: int, button_a_y: int, button_b_x: int, button_b_y: int) -> int:
    determinant = button_a_x*button_b_y - button_a_y*button_b_x
    if determinant == 0:
        return 0
    r = (prize_coords[0]*button_b_y - prize_coords[1]*button_b_x) / determinant
    s = (button_a_x*prize_coords[1] - button_a_y*prize_coords[0]) / determinant
    if r >= 0 and s >= 0 and r.is_integer() and s.is_integer():
        return int(3*r+s)
    return 0


total_p1 = 0
total_p2 = 0
for machine in tqdm(machines):
    _ = machine[-1].split(": ")[1].split(",")
    prize_coords = int(_[0].split("=")[1]), int(_[1].split("=")[1])
    button_a_values = machine[0].split(": ")[1].split(",")
    button_a_x = int(button_a_values[0].split("X")[1])
    button_a_y = int(button_a_values[1].split("Y")[1])
    button_b_values = machine[1].split(": ")[1].split(",")
    button_b_x = int(button_b_values[0].split("X")[1])
    button_b_y = int(button_b_values[1].split("Y")[1])

    printd(prize_coords, f"Button A: X+= {button_a_x}, Y+= {button_a_y}", "", f"Button B: X+= {button_b_x}, Y+= {button_b_y}")

    # find all combinations or r,s such that $r*button_a_x + s*button_b_x = prize_coords[0]$
    # then check if any of those satisfy $r*button_a_y + s*button_b_y = prize_coords[1]$

    max_r = prize_coords[0] // button_a_x
    max_r = max(max_r, 100)
    max_s = prize_coords[0] // button_b_x
    max_s = max(max_s, 100)

    lowest_token_found = float("inf")
    for r in range(max_r):
        for s in range(max_s):
            if r*button_a_x + s*button_b_x == prize_coords[0]:
                if r*button_a_y + s*button_b_y == prize_coords[1]:
                    if 3*r+s < lowest_token_found:
                        lowest_token_found = 3*r+s
                    else:
                        break
    if lowest_token_found == float("inf"):
        printd("No solution found")
    else:
        total_p1 += lowest_token_found
    
    total_p2 += lowest_tokens((prize_coords[0]+10000000000000, prize_coords[1]+10000000000000), button_a_x, button_a_y, button_b_x, button_b_y)
    


print("Part 1:", total_p1)
print("Part 2:", total_p2)