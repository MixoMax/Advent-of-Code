# Advent of Code 2024: Day 2
# @Author: Linus Horn

def solve_day_2(data: list[str]) -> tuple[int, int]:
    is_report_safe = lambda report: all((0 < (d := report[i] - report[i - 1]) < 4 or -4 < d < 0) and (d > 0) == ((report[1] - report[0]) > 0) for i in range(1, len(report)))
    is_report_safe_with_dampener = lambda report: any(is_report_safe(report[:i] + report[i+1:]) for i in range(len(report)))

    res = [
        is_report_safe([int(x) for x in data[idx//2].split()])
        if idx % 2 == 0 else is_report_safe_with_dampener([int(x)
        for x in data[idx//2].split()])
        for idx in range(len(data)*2)
        ]

    return sum(res[::2]), sum(res[1::2])

if __name__ == "__main__":
    from aoc import get_data
    data = get_data(2, splitlines=True)

    result = solve_day_2(data)
    print(f"Part 1: {result[0]}")
    print(f"Part 2: {result[1]}")
