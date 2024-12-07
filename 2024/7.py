# Advent of Code 2024: Day 7
from aoc import get_data
data = get_data(7, splitlines=True)

import itertools
from tqdm import tqdm

equations = {}
for line in data:
    # line: "x: 1 2 3"
    k, v = line.split(": ")
    v = [int(x) for x in v.split(" ")]
    equations[k] = v

def _eval(equation):
    parts = equation.split(" ")
    # parts: ["1", "+", "2", "*", "3"]
    # we dont need to worry about order of operations
    # evaluate from left to right
    result = int(parts[0])
    for i in range(1, len(parts), 2):
        if parts[i] == "+":
            result += int(parts[i+1])
        elif parts[i] == "*":
            result *= int(parts[i+1])
    return result

def _eval2(equation):
    parts = equation.split(" ")
    # parts: ["1", "+", "2", "*", "3"]
    # we dont need to worry about order of operations
    # evaluate from left to right
    result = int(parts[0])
    for i in range(1, len(parts), 2):
        if parts[i] == "+":
            result += int(parts[i+1])
        elif parts[i] == "*":
            result *= int(parts[i+1])
        elif parts[i] == "||":
            result = int(str(result) + str(parts[i+1]))
    return result
            

def is_possible(equations, k):
    equation = equations[k]
    opertions = ["+", "*"]
    # find all possible combinations of operations
    for ops in itertools.product(opertions, repeat=len(equation)-1):
        # ops: ["+", "*"]
        # create a new equation with the operations
        eq_str = ""
        for i in range(len(equation)-1):
            eq_str += str(equation[i]) + " " + ops[i] + " "
        eq_str += str(equation[-1])
        # evaluate the equation
        result = _eval(eq_str)
        if result == int(k):
            return True
    return False

def is_possible2(equations, k):
    equation = equations[k]
    opertions = ["+", "*", "||"]
    # find all possible combinations of operations
    for ops in itertools.product(opertions, repeat=len(equation)-1):
        # ops: ["+", "*"]
        # create a new equation with the operations
        eq_str = ""
        for i in range(len(equation)-1):
            eq_str += str(equation[i]) + " " + ops[i] + " "
        eq_str += str(equation[-1])
        
        # evaluate the equation
        result = _eval2(eq_str)
        if result == int(k):
            return True
    return False

s = 0
for k in equations:
    if is_possible(equations, k):
        s += int(k)
print(s)


s2 = 0
for k in tqdm(equations):
    if is_possible2(equations, k):
        s2 += int(k)
print(s2)
