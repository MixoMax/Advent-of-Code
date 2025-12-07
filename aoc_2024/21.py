# Advent of Code 2024: Day 21
from aoc import get_data, printd, set_debug
from functools import lru_cache

set_debug(True)

data: list[str] = get_data(day_num=21, splitlines=True)

# KEYPAD:
# 7 8 9
# 4 5 6
# 1 2 3
#   0 A
#
# A = Enter

KEYPAD = {
    "7": 0+0j, "8": 1+0j, "9": 2+0j,
    "4": 0+1j, "5": 1+1j, "6": 2+1j,
    "1": 0+2j, "2": 1+2j, "3": 2+2j,
    "X": 0+3j, "0": 1+3j, "A": 2+3j
}

# Arrow key pad
#   ^ A
# < v >
#
# A = Enter
ARROW_KEYPAD = {
    "X": 0+0j, "^": 1+0j, "A": 2+0j,
    "<": 0+1j, "v": 1+1j , ">": 2+1j
}

def path(start_str, end_str):
    keypad = KEYPAD if (start_str in KEYPAD and end_str in KEYPAD) else ARROW_KEYPAD

    start = keypad[start_str]
    end = keypad[end_str]
    delta = end - start
    dx, dy = int(delta.real), int(delta.imag)
    y_steps = ("^" * -dy) + ("v" * dy)
    x_steps = ("<" * -dx) + (">" * dx)
    
    bad = keypad["X"] - start
    do_y_first = (dx>0 or bad == dx) and bad != dy*1j
    if do_y_first:
        return y_steps + x_steps + "A"
    else:
        return x_steps + y_steps + "A"


@lru_cache(maxsize=None)
def length_of_sequence_for_code(code: str, depth: int):
    if depth == 0: return len(code)

    s = 0
    for idx, char in enumerate(code):
        s += length_of_sequence_for_code(path(code[idx-1], char), depth-1)
    return s

s = 0
for code in data:
    l = length_of_sequence_for_code(code, 3)
    complexity = int(code[:-1]) * l
    printd(f"Code: {code}, Length: {l}, Complexity: {complexity}")
    s += complexity
print(s)

s = 0
for code in data:
    l = length_of_sequence_for_code(code, 26)
    complexity = int(code[:-1]) * l
    printd(f"Code: {code}, Length: {l}, Complexity: {complexity}")
    s += complexity
print(s)