# Advent of Code 2024: Day 1
# @Author: Linus Horn


def solve_day_1(data: list[str]) -> tuple[int, int]:
    l1 = []
    l2 = []
    ret = []

    for line in data:
        v1, v2 = line.split("   ")
        l1.append(int(v1))
        l2.append(int(v2))

    l1 = sorted(l1)
    l2 = sorted(l2)

    # Part 1
    diff = sum([abs(l1[i] - l2[i]) for i in range(len(l1))])

    ret.append(diff)


    # Part 2

    score = 0
    for n in l1:
        score += n*l2.count(n)


    ret.append(score)

    return tuple(ret)

if __name__ == "__main__":
    from .aoc import get_data

    data = get_data(1, splitlines=True)

    
    result = solve_day_1(data)
    print(f"Part 1: {result[0]}")
    print(f"Part 2: {result[1]}")
