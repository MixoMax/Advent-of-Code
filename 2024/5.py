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

# Parse input
data = get_data(5, splitlines=False)
rules_section, updates_section = data.strip().split('\n\n')

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

print(s_p1)


# Calculate result
result = sum(update[len(update)//2] for update in incorrect_updates)
print(result)
