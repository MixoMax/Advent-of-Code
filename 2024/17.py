# Advent of Code 2024: Day 17
from aoc import get_data, printd, set_debug, get_debug
set_debug(True)
data = get_data(17, splitlines=True, year_num=2024)

global isnatructionj_pointer, output, reg_A, reg_B, reg_C, mem

instruction_pointer = 0

output = []

reg_A = int(data[0].split(": ")[1])
reg_B = int(data[1].split(": ")[1])
reg_C = int(data[2].split(": ")[1])


mem = [int(x) for x in data[3].split(": ")[1].split(",")]


printd(f"{reg_A=}, {reg_B=}, {reg_C=}, {mem=}")

def get_operand():
    global instruction_pointer, mem
    return mem[instruction_pointer+1]

def get_combo_operand():
    global instruction_pointer, mem
    operand = get_operand()

    if operand in list(range(0, 4)):
        return operand
    else:
        match operand:
            case 4:
                return reg_A
            case 5:
                return reg_B
            case 6:
                return reg_C
            case _:
                raise ValueError(f"Invalid operand: {operand}")



def adv():
    global reg_A, reg_B, reg_C, mem, instruction_pointer
    
    operand = get_combo_operand()
    denom = 2**operand
    
    numerator = reg_A
    printd(f"Setting reg_A to {numerator} // {denom} = {numerator // denom}")
    reg_A = numerator // denom

    instruction_pointer += 2

def bxl():
    global reg_A, reg_B, reg_C, mem, instruction_pointer
    
    operand = get_operand()

    printd(f"Setting reg_B to {reg_B} ^ {operand} = {reg_B ^ operand}")

    # bitwise xor of reg_B and operand
    reg_B = reg_B ^ operand

    instruction_pointer += 2

def bst():
    global reg_A, reg_B, reg_C, mem, instruction_pointer
    
    operand = get_combo_operand()

    printd(f"Setting reg_B to {operand} % 8 = {operand % 8}")

    reg_B = operand % 8

    instruction_pointer += 2

def jnz():
    global reg_A, reg_B, reg_C, mem, instruction_pointer

    operand = get_operand()

    if reg_A == 0:
        instruction_pointer += 2
        return
    
    printd(f"Jumping to {operand}")
    
    instruction_pointer = operand

def bxc():
    global reg_A, reg_B, reg_C, mem, instruction_pointer

    # bitwise xor of reg_B and reg_C

    printd(f"Setting reg_B to {reg_B} ^ {reg_C} = {reg_B ^ reg_C}")

    reg_B = reg_B ^ reg_C

    instruction_pointer += 2

def out():
    global reg_A, reg_B, reg_C, mem, instruction_pointer, output

    operand = get_combo_operand()

    output.append(operand % 8)

    instruction_pointer += 2

def bdv():
    global reg_A, reg_B, reg_C, mem, instruction_pointer
    # just like adv, but store the result in reg_B

    operand = get_combo_operand()

    numerator = reg_A
    denom = 2**operand

    printd(f"Setting reg_B to {numerator} // {denom} = {numerator // denom}")

    reg_B = numerator // denom

    instruction_pointer += 2

def cdv():
    global reg_A, reg_B, reg_C, mem, instruction_pointer
    # just like adv, but store the result in reg_C

    operand = get_combo_operand()

    numerator = reg_A
    denom = 2**operand

    printd(f"Setting reg_C to {numerator} // {denom} = {numerator // denom}")

    reg_C = numerator // denom

    instruction_pointer += 2



opcodes = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}


# DEBUG
# mem = [0,1,5,4,3,0]
# reg_A = 2024
# reg_B = 0
# reg_C = 0

while instruction_pointer < len(mem):
    opcode = mem[instruction_pointer]
    printd(f"{instruction_pointer=} {opcode=} {opcodes[opcode].__name__}")
    opcodes[opcode]()
    printd(f"{reg_A=}, {reg_B=}, {reg_C=}, {mem=}, {output=}")
    input()

print(",".join([str(x) for x in output]))
