# @Author: Linus Horn
import os

def get_data(day_num: int, splitlines: bool = True) -> str | list[str]:
    if not os.path.exists(f"./data/{day_num}.txt"):
        print(f"Data for day {day_num} not found.")
        print(f"If you cloned this from GitHub, make sure to create ,/data/{day_num}.txt and paste your puzzle input there.")
        raise FileNotFoundError


    with open(f"./data/{day_num}.txt") as f:
        data = f.read()
    if splitlines:
        return data.split("\n")
    return data
