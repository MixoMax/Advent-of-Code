# Advent of Code 2024: Day 5
# @Author: Linus Horn
from aoc import get_data


def is_valid_order(sequence, rules):
    sequence = [int(x) for x in sequence]
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            first, second = sequence[i], sequence[j]
            if [second, first] in rules:
                return False
    return True

def compare_pages(a, b, rules):
    # Returns True if a should come before b
    if [b, a] in rules:
        return False
    if [a, b] in rules:
        return True
    return a < b  # Default comparison if no direct rule exists

def sort_sequence(sequence, rules):
    # Convert sequence to integers
    sequence = [int(x) for x in sequence]
    # Sort sequence
    
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if not compare_pages(sequence[i], sequence[j], rules):
                sequence[i], sequence[j] = sequence[j], sequence[i]

    return sequence

def solve_day_5(data: list[str]) -> tuple[int, int]:
    rules_section, updates_section = "\n".join(data).strip().split('\n\n')
    ret = []

    # Parse rules
    rules = []
    for line in rules_section.split('\n'):
        a, b = line.split('|')
        rules.append([int(a), int(b)])

    # Find incorrect updates and sort them
    s_p1 = 0
    incorrect_updates = []
    for line in updates_section.split('\n'):
        sequence = line.strip().split(',')
        if not is_valid_order(sequence, rules):
            sorted_sequence = sort_sequence(sequence, rules)
            incorrect_updates.append(sorted_sequence)
        else:
            s_p1 += int(sequence[len(sequence)//2])

    ret.append(s_p1)


    # Calculate result
    result = sum(update[len(update)//2] for update in incorrect_updates)
    ret.append(result)

    return tuple(ret) #type: ignore

if __name__ == "__main__":
    from aoc import get_data
    data = get_data(5, splitlines=True)
    result = solve_day_5(data)
    print(f"Part 1: {result[0]}, Part 2: {result[1]}")