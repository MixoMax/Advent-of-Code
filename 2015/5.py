# Advent of Code 2015: Day 5
# @Author: Linus Horn

from aoc import get_data

data = get_data(5)

vowels = "aeiou"
letters = "abcdefghijklmnopqrstuvwxyz"

def is_nice_str(s:str) -> bool:
    global vowels, letters

    forbidden_combinations = ["ab", "cd", "pq", "xy"]

    n_vowels = sum([s.count(v) for v in vowels])
    doesnt_have_forbidden_combinations = not any([fc in s for fc in forbidden_combinations])
    has_double_letter = any([l+l in s for l in letters])

    return n_vowels >= 3 and doesnt_have_forbidden_combinations and has_double_letter

# Part 1
n_nice_strings = 0
for line in data.split("\n"):
    if is_nice_str(line):
        n_nice_strings += 1
print(n_nice_strings)


# Part 2

def is_nice_str_2(s:str) -> bool:
    global vowels, letters

    two_char_combinations = [s[i] + s[i+1] for i in range(len(s) - 1)]
    r1 = False
    for idx in range(len(two_char_combinations)):
        idx = len(two_char_combinations) - idx - 1
        tcc = two_char_combinations[idx]
        if two_char_combinations.count(tcc) > 1:
            other_idx = two_char_combinations.index(tcc)
            if abs(idx - other_idx) > 1:
                r1 = True


    r2 = False
    for idx in range(len(s) - 2):
        idx = idx + 2
        if s[idx-2] == s[idx]:
            r2 = True

    return r1 and r2

# Part 1
n_nice_strings = 0
for line in data.split("\n"):
    if is_nice_str_2(line):
        n_nice_strings += 1
print(n_nice_strings)