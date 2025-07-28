# Advent of Code 2024: Day 4
# @Author: Linus Horn



def count_xmas(data: list[str]) -> int:
    rows = len(data)
    cols = len(data[0])
    count = 0
    
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)
    ]
    
    def check_xmas(row: int, col: int, dx: int, dy: int) -> bool:
        if (0 <= row + 3*dx < rows and 
            0 <= col + 3*dy < cols):
            return (data[row][col] == "X" and 
                   data[row + dx][col + dy] == "M" and 
                   data[row + 2*dx][col + 2*dy] == "A" and 
                   data[row + 3*dx][col + 3*dy] == "S")
        return False
    
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_xmas(i, j, dx, dy):
                    count += 1
    
    return count


# Part 2

# find MAS in the shape of an X

def count_x_mas(data: list[str]) -> int:
    rows = len(data)
    cols = len(data[0])
    count = 0
    
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if data[i][j] == "A":
                if (
                    ((data[i-1][j-1] == "M" and data[i+1][j+1] == "S") or
                     (data[i-1][j-1] == "S" and data[i+1][j+1] == "M")) and
                    ((data[i-1][j+1] == "M" and data[i+1][j-1] == "S") or
                     (data[i-1][j+1] == "S" and data[i+1][j-1] == "M"))
                ):
                    count += 1
    
    return count


def solve_day_4(data: list[str]) -> tuple[int, int]:
    part_1 = count_xmas(data)
    part_2 = count_x_mas(data)
    return part_1, part_2

if __name__ == "__main__":
    from aoc import get_data
    data = get_data(4, splitlines=True)
    part_1, part_2 = solve_day_4(data)
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")