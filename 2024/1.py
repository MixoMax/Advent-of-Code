# Advent of Code 2024: Day 1
# @Author: Linus Horn

from aoc import get_data

data = get_data(1, splitlines=True)

l1 = []
l2 = []

for line in data:
    v1, v2 = line.split("   ")
    l1.append(int(v1))
    l2.append(int(v2))

l1 = sorted(l1)
l2 = sorted(l2)

# Part 1
diff = sum([abs(l1[i] - l2[i]) for i in range(len(l1))])

print(diff)


# Part 2

score = 0
for n in l1:
    score += n*l2.count(n)


print(score)