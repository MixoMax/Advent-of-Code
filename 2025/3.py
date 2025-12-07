from aoc import get_data
data_lines, data_str = get_data(3, year_num=2025) # read in the input once split by lines and as a raw string
total_output_joltage = 0

for line in data_lines:
    # Ensure the line has content
    if not line.strip():
        continue
        
    # Convert the string of digits into a list of integers
    digits = [int(d) for d in line.strip()]
    
    current_bank_max = 0
    
    for tens_candidate in range(9, 0, -1):
        try:
            first_index = digits.index(tens_candidate)
        except ValueError:
            continue
            
        if first_index < len(digits) - 1:
            remaining_batteries = digits[first_index + 1:]
            ones_candidate = max(remaining_batteries)
            
            current_bank_max = tens_candidate * 10 + ones_candidate
            break
            
    total_output_joltage += current_bank_max

print(total_output_joltage)

total_output_joltage = 0
REQUIRED_LENGTH = 12

for line in data_lines:
    digits = [int(d) for d in line.strip()]
    n = len(digits)

    stack = []
    
    for i, d in enumerate(digits):
        # Calculate how many digits are left in the input after the current one
        remaining_in_input = n - 1 - i
        
        # We want to maintain a decreasing stack (largest digits first) as much as possible.
        # Check if we can improve the sequence by replacing the last chosen digit with the current one.
        # Condition to pop:
        # 1. Stack is not empty
        # 2. Current digit 'd' is larger than stack[-1]
        # 3. We can afford to discard the last picked digit and still reach length 12
        while stack and stack[-1] < d:
            if len(stack) + remaining_in_input >= REQUIRED_LENGTH:
                stack.pop()
            else:
                break
        
        # we need more digits!
        if len(stack) < REQUIRED_LENGTH:
            stack.append(d)
            

    if len(stack) == REQUIRED_LENGTH:
        bank_value = int("".join(map(str, stack)))
        total_output_joltage += bank_value

print(total_output_joltage)

  