# Advent of Code 2015: Day 3
# @Author: Linus Horn

from aoc import get_data

data = get_data(3)

pos = [0,0]
visited_positions = [(0,0)]

for char in data:
    match char:
        case "^": pos[1] = pos[1] + 1
        case "v": pos[1] = pos[1] - 1
        case ">": pos[0] = pos[0] + 1
        case "<": pos[0] = pos[0] - 1
    
    visited_positions.append((pos[0], pos[1]))

print(len(set(visited_positions)))


pos_1 = [0,0]
pos_2 = [0,0]
visited_positions = [(0,0)]

for idx, char in enumerate(data):
    if idx % 2 == 0:
        match char:
            case "^": pos_1[1] = pos_1[1] + 1
            case "v": pos_1[1] = pos_1[1] - 1
            case ">": pos_1[0] = pos_1[0] + 1
            case "<": pos_1[0] = pos_1[0] - 1
        
        visited_positions.append((pos_1[0], pos_1[1]))
    else:
        match char:
            case "^": pos_2[1] = pos_2[1] + 1
            case "v": pos_2[1] = pos_2[1] - 1
            case ">": pos_2[0] = pos_2[0] + 1
            case "<": pos_2[0] = pos_2[0] - 1
        
        visited_positions.append((pos_2[0], pos_2[1]))

print(len(set(visited_positions)))