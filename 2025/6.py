from aoc import get_data
data_lines, data_str = get_data(6, year_num=2025, strip=False)

num_lists = []
for line in data_lines[:-1]:
    nums = [int(x) for x in line.split()]
    num_lists.append(nums)

operations = data_lines[-1].split()

s = 0
for idx in range(len(num_lists[0])):
    nums = [num_lists[row][idx] for row in range(len(num_lists))]
    if operations[idx] == "+":
        s += sum(nums)
    elif operations[idx] == "*":
        prod = 1
        for n in nums:
            prod *= n
        s += prod
print(s)


n_problems = len(data_lines[0].split())
last_line = data_lines[-1]
widths = [0] * n_problems
current_width = 0
current_problem_idx = 0
for ch in last_line[1:]:
    if ch in "+*":
        widths[current_problem_idx] = current_width
        current_problem_idx += 1
        current_width = 0
    else:
        current_width += 1
widths[current_problem_idx] = current_width + 1

math_problems = [[] for _ in range(n_problems)]
for line in data_lines[:-1]:
    start_idx = 0
    for problem_idx in range(n_problems):
        width = widths[problem_idx]
        problem_str = line[start_idx:start_idx + width]
        math_problems[problem_idx].append(problem_str)
        start_idx += width + 1  # +1 for the space

print(math_problems)

nums_rotated = [[] for _ in range(n_problems)]
for problem_idx in range(n_problems):
    width = widths[problem_idx]
    for char_idx in range(width):
        chars = [math_problems[problem_idx][row][char_idx] for row in range(len(math_problems[problem_idx]))]
        num_str = "".join(chars).strip()
        nums_rotated[problem_idx].append(int(num_str))
print(nums_rotated)

s = 0
for idx in range(n_problems):
    nums = nums_rotated[idx]
    if operations[idx] == "+":
        s += sum(nums)
    elif operations[idx] == "*":
        prod = 1
        for n in nums:
            prod *= n
        s += prod
print(s)