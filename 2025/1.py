from aoc import get_data, printd, set_debug
from tqdm import tqdm

set_debug(False)

data_lines, data_str = get_data(1, year_num=2025)

n = 50
number_of_0 = 0
for line in data_lines:
    turning_direction = line[0]
    distance = int(line[1:])
    if turning_direction == "R":
        n += distance
    else:
        n -= distance
    
    # only numbers from 0 to 99, so we wrap around
    n = n % 100
    if n == 0:
        number_of_0 += 1

print(number_of_0)

# part 2

n = 50
number_of_0_overflown = 0
for line in tqdm(data_lines):
    turning_direction = line[0]
    distance = int(line[1:])
    
    if turning_direction == "R":
        new_n = n + distance
        # Count multiples of 100 in range (n, new_n]
        count = new_n // 100
    else:
        new_n = n - distance
        # Count multiples of 100 in range [new_n, n-1]
        count = (n - 1) // 100 - (new_n - 1) // 100
    
    number_of_0_overflown += count
    n = new_n % 100

print(number_of_0_overflown)