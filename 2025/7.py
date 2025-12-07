from aoc import get_data
from collections import defaultdict

data_lines, data_str = get_data(7, year_num=2025)

start_row = data_lines[0]
print(start_row)
beam_positions = {start_row.index("S")}

n_splits = 0
for row in data_lines[1:]:
    for bp in list(beam_positions):
        if bp < 0 or bp >= len(row):
            beam_positions.remove(bp)
            continue
        cell_val = row[bp]
        if cell_val == "^":
            beam_positions.remove(bp)
            beam_positions.add(bp - 1)
            beam_positions.add(bp + 1)
            n_splits += 1

print(n_splits) # part 1 done


start_col = start_row.index("S")
grid_width = len(start_row)

# Using a dictionary to track counts of timelines at each column
# Key: column index, Value: number of timelines at that column
counts = defaultdict(int)
counts[start_col] = 1
    
for row in data_lines[1:]:
    next_counts = defaultdict(int)
    
    for col, count in counts.items():
        # Filter out timelines that have gone out of horizontal bounds
        if col < 0 or col >= grid_width:
            continue
        
        char = row[col]
        
        if char == '^':
            # Splitter: The timeline splits into two.
            # One branch goes left, one branch goes right.
            next_counts[col - 1] += count
            next_counts[col + 1] += count
        else:
            # Empty space (or other): The timeline continues straight down.
            next_counts[col] += count
    
    counts = next_counts

total_timelines = 0
for col, count in counts.items():
    if 0 <= col < grid_width:
        total_timelines += count
print(total_timelines)  # part 2 done