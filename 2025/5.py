from aoc import get_data
from tqdm import tqdm
data_lines, data_str = get_data(5, year_num=2025)

fresh_id_ranges_str, availible_ids_str = data_str.split("\n\n")
fresh_id_ranges: list[tuple[int, int]] = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in fresh_id_ranges_str.split("\n")]
availible_ids = list(map(int, availible_ids_str.split("\n")))

n_fresh = 0
for availible_id in tqdm(availible_ids):
    for fresh_id_range in fresh_id_ranges:
        if fresh_id_range[0] <= availible_id <= fresh_id_range[1]:
            n_fresh += 1
            break
print(n_fresh)

# part 2

# join overlapping id ranges
# for example (1-3) and (2-4) become (1-4)
# operate on the fresh_id_ranges list, so we do not have to do any iterations
fresh_id_ranges.sort()
merged_ranges = []
current_start, current_end = fresh_id_ranges[0]
for start, end in fresh_id_ranges[1:]:
    if start <= current_end:
        current_end = max(current_end, end)
    else:
        merged_ranges.append((current_start, current_end))
        current_start, current_end = start, end
merged_ranges.append((current_start, current_end))
n_fresh = 0
for id_range in merged_ranges:
    n_fresh += abs(id_range[1] - id_range[0]) + 1
print(n_fresh)