

def get_data(day_num: int) -> str:
    with open(f"./data/{day_num}.txt") as f:
        return f.read()