# Advent of Code 2015: Day 4
# @Author: Linus Horn

from r import get_data

data = get_data(4)

from hashlib import md5
from tqdm import tqdm

base_key = data

# Part 1
for i in tqdm(range(100_000_000)):
    k = base_key + str(i)
    h = md5(k.encode()).hexdigest()
    if h.startswith("00000"):
        print(i)
        break

# Part 2
for i in tqdm(range(100_000_000)):
    k = base_key + str(i)
    h = md5(k.encode()).hexdigest()
    if h.startswith("000000"):
        print(i)
        break