# Advent of Code 2024: Day 22
# @Author: Linus Horn
from functools import cache
import itertools

with open("./data/22.txt") as f:
    data: list[str] = f.read().splitlines()

@cache
def next_secret_num(num: int) -> int:
    # Step 1: multiply by 64
    result = num * 64
    num = result ^ num  # mix
    num = num % 16777216  # prune

    # Step 2: divide by 32 and round down
    result = num // 32
    num = result ^ num  # mix
    num = num % 16777216  # prune

    # Step 3: multiply by 2048
    result = num * 2048
    num = result ^ num  # mix
    num = num % 16777216  # prune

    return num

n_iterations = 2_000

s_total = 0
changes = []
nums = []
for num in data:
    num = int(num)
    nums.append([num])
    changes.append([])
    for _ in range(n_iterations):
        new_num = next_secret_num(num)
        changes[-1].append(int(str(new_num)[-1]) - int(str(num)[-1]))
        nums[-1].append(int(str(new_num)[-1]))
        num = new_num
    s_total += num

print("Part 1:", s_total)




# Part 2
best_score = 0
for (a,b,c,d) in itertools.product(range(-9,10), repeat=4):
    score = 0
    for i in range(len(nums)):
        best_score_for_i = 0
        # find each subsequence of changes[i] that is [a,b,c,d]
        for j in range(len(changes[i])):
            #print(changes[i][j:j+4])
            if changes[i][j:j+4] == [a,b,c,d]:
                best_score_for_i = max(best_score_for_i, nums[i][j+4])
        score += best_score_for_i
    best_score = max(best_score, score)

print("Part 2:", best_score)
