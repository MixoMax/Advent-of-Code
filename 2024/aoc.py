# aoc.py
# @Description: Helper functions for Advent of Code 2024
# @Author: Linus Horn
import os
import re

DEBUG = False

def get_data(day_num: int, splitlines: bool = True, year_num: int = -1) -> list[str] | str:
    if year_num != -1:
        fp = f"./{year_num}/data/{day_num}.txt"
        if not os.path.exists(fp):
            fp = f"./data/{day_num}.txt"
    else:
        fp = f"./data/{day_num}.txt"
    if not os.path.exists(fp):
        print(f"Data for day {day_num} not found.")
        print(f"If you cloned this from GitHub, make sure to create {fp} and paste your puzzle input there.")
        raise FileNotFoundError


    with open(fp) as f:
        data = f.read()
    if splitlines:
        data = data.splitlines()
        return [line.rstrip() for line in data if line.strip()]
    return data.rstrip()


def printd(*args):
    if DEBUG:
        print(*args)

def set_debug(debug: bool):
    global DEBUG
    DEBUG = debug

def get_debug():
    global DEBUG
    return DEBUG

num_re = re.compile(r"-?\d+")

