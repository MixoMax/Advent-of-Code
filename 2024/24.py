# Advent of Code 2024: Day 24
# @Author: Linus Horn
from aoc import get_data, printd, set_debug, get_debug, nums
from tqdm import tqdm
from functools import cache
import itertools

set_debug(True)
data: str = get_data(day_num=24, splitlines=False)

variable_part, logic_part = data.split("\n\n")

variables = {}
for line in variable_part.split("\n"):
    key, value = line.split(": ")
    value = int(value)
    variables[key] = value

AND = lambda a, b: int(a==1 and b==1)
OR = lambda a, b: int(a==1 or b==1)
XOR = lambda a, b: int(a!=b)

expressions = [] # list of tuples (input_1, input_2, operator, output)

for line in logic_part.split("\n"):
    # eg: x00 AND y00 -> z00
    inputs, output = line.split(" -> ")
    inputs = inputs.split(" ")
    input_1, operator, input_2 = inputs
    operator = operator.upper()
    output = output.strip()
    expressions.append((input_1, input_2, operator, output))

to_remove = []
while expressions:
    for expression in expressions:
        if expression[0] in variables and expression[1] in variables:
            # can calculate this expression because all dependencies are known
            input_1 = variables[expression[0]]
            input_2 = variables[expression[1]]
            operator = expression[2]
            output = expression[3]
            match operator:
                case "AND":
                    variables[output] = AND(input_1, input_2)
                case "OR":
                    variables[output] = OR(input_1, input_2)
                case "XOR":
                    variables[output] = XOR(input_1, input_2)
                case _:
                    print("Unknown operator")
            to_remove.append(expression)
    expressions = list(set(expressions) - set(to_remove))
    to_remove = []


max_z_value = 0
for key in variables:
    if key.startswith("z"):
        max_z_value = max(max_z_value, int(key.replace("z", "")))

out_bits = [0 for _ in range(max_z_value+1)]
for key in variables:
    if key.startswith("z"):
        out_bits[int(key.replace("z", ""))] = variables[key]

bit_str = "".join(map(str, out_bits))[::-1]
print(bit_str)
print(int(bit_str, 2))