# Advent of Code 2015: Day 7
# @Author: Linus Horn

from aoc import get_data
data = get_data(7, splitlines=False)


def evaluate_wire(wire, circuit, cache):
    # If the wire value is already cached, return it
    if wire in cache:
        return cache[wire]
    
    # If the wire is a numeric string, return its integer value
    if wire.isdigit():
        return int(wire)
    
    # Get the instruction for this wire
    instruction = circuit[wire]
    
    # Parse the instruction and evaluate accordingly
    parts = instruction.split()
    
    if len(parts) == 1:
        # Simple assignment: "123 -> x" or "b -> a"
        value = evaluate_wire(parts[0], circuit, cache)
    
    elif len(parts) == 2:
        # NOT operation: "NOT x -> y"
        assert parts[0] == "NOT"
        value = ~evaluate_wire(parts[1], circuit, cache) & 0xFFFF
    
    else:  # len(parts) == 3
        # Binary operations: AND, OR, LSHIFT, RSHIFT
        left = evaluate_wire(parts[0], circuit, cache)
        right = evaluate_wire(parts[2], circuit, cache)
        
        if parts[1] == "AND":
            value = left & right
        elif parts[1] == "OR":
            value = left | right
        elif parts[1] == "LSHIFT":
            value = (left << right) & 0xFFFF
        elif parts[1] == "RSHIFT":
            value = (left >> right) & 0xFFFF
    
    # Cache the result and return
    cache[wire] = value
    return value

def parse_input(input_text):
    circuit = {}
    for line in input_text.strip().split('\n'):
        instruction, wire = line.split(' -> ')
        circuit[wire] = instruction
    return circuit

def solve_1(input_text):
    circuit = parse_input(input_text)
    cache = {}
    evals = {}
    for wire in circuit:
        value = evaluate_wire(wire, circuit, cache)
        evals[wire] = value
    return evals["a"]

def solve_2(input_text):
    circuit = parse_input(input_text)
    cache = {}
    val_a = solve_1(input_text)

    # Take the signal from wire "a" and override wire "b" with it
    # then re-evaluate all other wires (including "a")
    circuit = {**circuit, "b": str(val_a)}
    cache = {}
    evals = {}
    for wire in circuit:
        value = evaluate_wire(wire, circuit, cache)
        evals[wire] = value
    return evals["a"]




# Solve the puzzle
result = solve_1(data)
print(result)

result = solve_2(data)
print(result)