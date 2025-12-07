from aoc import get_data
data_lines, data_str = get_data(2, year_num=2025)

is_invalid_id = lambda n: (s := str(n))[:len(str(n))//2] == s[len(str(n))//2:] if len(str(n)) % 2 == 0 else False
is_invalid_id_2 = lambda n: any((s := str(n))[:m] * (len(str(n)) // m) == s for m in range(1, len(str(n)) // 2 + 1) if len(str(n)) % m == 0)

s_1 = s_2 = 0
for id_Range_str in data_str.split(","):
    first, last = map(int, id_Range_str.split("-"))
    s_1 += sum(id_num for id_num in range(first, last + 1) if is_invalid_id(id_num))
    s_2 += sum(id_num for id_num in range(first, last + 1) if is_invalid_id_2(id_num))
print(s_1, s_2, sep="\n")