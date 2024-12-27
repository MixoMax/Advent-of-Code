# Advent of Code 2024: Day 21
from aoc import get_data, printd, set_debug, get_debug, nums
from collections import deque
from typing import Dict, List, Set, Tuple

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
    "7": (0, 3), "8": (1, 3), "9": (2, 3),
    "4": (0, 2), "5": (1, 2), "6": (2, 2),
    "1": (0, 1), "2": (1, 1), "3": (2, 1),
                 "0": (1, 0), "A": (2, 0)
}

# Arrow key pad
#   ^ A
# < v >
#
# A = Enter
ARROW_KEYPAD = {
                 "^": (1, 1), "A": (2, 1),
    "<": (0, 0), "v": (1, 0), ">": (2, 0)
}

def sequence_for_code(code:str) -> str:
    # calculate the sequence of movements (<^>vA) for a given code
    # (<^>v) are the directions, A means press the button
    # starting position is always hovering over A

    start_pos = KEYPAD["A"]
    def sequence_for_move(start_pos: tuple[int, int], end_pos: tuple[int, int]) -> str:
        # calculate the sequence of movements (<^>v) for a given move
        if 0 not in start_pos:
            # start pos is 8,9,5,6,2 or 3
            # means, we can just move directly to the end pos
            delta_x = end_pos[0] - start_pos[0]
            delta_y = end_pos[1] - start_pos[1]
            out_str = ""
            if delta_x > 0:
                out_str += ">" * abs(delta_x)
            elif delta_x < 0:
                out_str += "<" * abs(delta_x)
            if delta_y > 0:
                out_str += "v" * abs(delta_y)
            elif delta_y < 0:
                out_str += "^" * abs(delta_y)
            return out_str + "A"
        else:
            # we can not hover over the empty space next to 0
            if start_pos[0] == 0:
                # start pos is 1,4 or 7
                # we need to move horizontally first, then vertically
                horizontal_first = True
            else:
                # start pos is 3,6 or 9
                # we need to move vertically first, then horizontally
                horizontal_first = False
            
            delta_x = end_pos[0] - start_pos[0]
            delta_y = end_pos[1] - start_pos[1]
            out_str = ""
            if horizontal_first:
                if delta_x > 0:
                    out_str += ">" * abs(delta_x)
                elif delta_x < 0:
                    out_str += "<" * abs(delta_x)
                if delta_y > 0:
                    out_str += "v" * abs(delta_y)
                elif delta_y < 0:
                    out_str += "^" * abs(delta_y)
            else:
                if delta_y > 0:
                    out_str += "v" * abs(delta_y)
                elif delta_y < 0:
                    out_str += "^" * abs(delta_y)
                if delta_x > 0:
                    out_str += ">" * abs(delta_x)
                elif delta_x < 0:
                    out_str += "<" * abs(delta_x)
            return out_str + "A"
    
    out_sequence = ""
    for target in code:
        target_pos = KEYPAD[target]
        out_sequence += sequence_for_move(start_pos, target_pos)
        start_pos = target_pos
    return out_sequence


def sequence_for_sequence(sequence: str) -> str:
    # calculate the sequence of movements (<^>vA) for a given sequence
    # (<^>v) are the directions, A means press the button
    # starting position is always hovering over A
    # basically the same as sequence_for_code, but use the Arrow key pad
    start_pos = ARROW_KEYPAD["A"]

    def sequence_for_move_2(start_pos: tuple[int, int], end_pos: tuple[int, int]) -> str:
        # calculate the sequence of movements (<^>v) for a given move
        if start_pos != (0,0) and end_pos != (0,0):
            # start_pos and end_pos are both not <, so we can move directly
            delta_x = end_pos[0] - start_pos[0]
            delta_y = end_pos[1] - start_pos[1]
            out_str = ""
            if delta_x > 0:
                out_str += ">" * abs(delta_x)
            elif delta_x < 0:
                out_str += "<" * abs(delta_x)
            if delta_y > 0:
                out_str += "v" * abs(delta_y)
            elif delta_y < 0:
                out_str += "^" * abs(delta_y)
            return out_str + "A"
        else:
            if start_pos == (0,0):
                # start_pos is <, so we need to move horizontally first
                horizontal_first = True
            else:
                # end_pos is <, so we need to move vertically first
                horizontal_first = False
            
            delta_x = end_pos[0] - start_pos[0]
            delta_y = end_pos[1] - start_pos[1]
            out_str = ""

            if horizontal_first:
                if delta_x > 0:
                    out_str += ">" * abs(delta_x)
                elif delta_x < 0:
                    out_str += "<" * abs(delta_x)
                if delta_y > 0:
                    out_str += "v" * abs(delta_y)
                elif delta_y < 0:
                    out_str += "^" * abs(delta_y)
            else:
                if delta_y > 0:
                    out_str += "v" * abs(delta_y)
                elif delta_y < 0:
                    out_str += "^" * abs(delta_y)
                if delta_x > 0:
                    out_str += ">" * abs(delta_x)
                elif delta_x < 0:
                    out_str += "<" * abs(delta_x)
            return out_str + "A"
    
    out_sequence = ""
    for target in sequence:
        target_pos = ARROW_KEYPAD[target]
        out_sequence += sequence_for_move_2(start_pos, target_pos)
        start_pos = target_pos
    return out_sequence

n_sum = 0
for code in data:
    seq = sequence_for_sequence(sequence_for_sequence(sequence_for_code(code)))
    printd(f"{code=} {seq=} {len(seq)=}")
    
    