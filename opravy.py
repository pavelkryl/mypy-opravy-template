from typing import List

# Mistake 1
def calculate_area(radius):
    pi = 3.14159
    return pi * radius * radius

# Mistake 2
def find_max(numbers: List[int]):
    max_value = None
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

# Mistake 3
def divide(a: int, b: int) -> str:
    result = a / b
    return result

# Mistake 4
def calculate_average(scores: List[float]) -> float:
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

# Mistake 5
def print_name_length(name: str):
    name_length = len(name)
    print(f"The name is {name_length} characters long.")
