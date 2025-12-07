import time
t_0 = time.time()

from aoc import get_data, printd, set_debug
data_lines, data_str = get_data(2, year_num=2025)

def is_invalid_id(n: int) -> bool:
    s = str(n)
    length = len(s)
    if length % 2 != 0:
        return False
    mid = length // 2
    return s[:mid] == s[mid:]

def is_invalid_id_2(n: int) -> bool:
    s = str(n)
    length = len(s)
    for m in range(1, length // 2 + 1):
        if length % m == 0:
            pattern = s[:m]
            multiplier = length // m
            if pattern * multiplier == s:
                return True
    return False


wrong_ids = []
wrong_ids_2 = []
for id_Range_str in data_str.split(","):
    first, last = map(int, id_Range_str.split("-"))
    for id_num in range(first, last + 1):
        if is_invalid_id(id_num):
            wrong_ids.append(id_num)
        if is_invalid_id_2(id_num):
            wrong_ids_2.append(id_num)
print(sum(wrong_ids))
print(sum(wrong_ids_2))
print(time.time() - t_0)