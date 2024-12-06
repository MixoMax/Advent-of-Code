# Advent of Code 2015: Day 10
# @Author: Linus Horn


def look_and_say(s):
    parts = []
    current = s[0]
    for c in s[1:]:
        if c == current[0]:
            current += c
        else:
            parts.append(current)
            current = c
    parts.append(current)

    num_str = ""
    for part in parts:
        num_str += str(len(part)) + part[0]
    return num_str

n = 40
s = "1321131112"
for _ in range(n):
    s = look_and_say(s)
print(len(s))


n = 50
s = "1321131112"
for _ in range(n):
    s = look_and_say(s)
print(len(s))
