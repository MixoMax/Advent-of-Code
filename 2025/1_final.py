from aoc import get_data
num_zeros_hit = num_zeros_overflown = 0
n = 50
for line in get_data(1, year_num=2025)[0]:
    turning_direction = line[0]
    new_n = n + (int(line[1:]) * (int(turning_direction == "R")*2-1))
    num_zeros_overflown += new_n // 100 if turning_direction == "R" else (n - 1) // 100 - (new_n - 1) // 100
    n = new_n % 100
    num_zeros_hit += int(n==0)
print(num_zeros_hit)
print(num_zeros_overflown)

