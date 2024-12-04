# @Author: Linus Horn

def get_data(day_num: int, splitlines: bool = True) -> str | list[str]:
    with open(f"./data/{day_num}.txt") as f:
        data = f.read()
    if splitlines:
        return data.split("\n")
    return data
