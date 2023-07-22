import random

def generate_random_number():
    return random.randint(0, 1000)

result = generate_random_number()
assert result >= 0, f"Error: Expected number >= 0, but got {result}"

result = generate_random_number()
assert result <= 1000, f"Error: Expected number <= 1000, but got {result}"

result = generate_random_number()
assert isinstance(result, int), f"Error: Expected integer, but got {type(result)}"

random_numbers = set()
for _ in range(100):
    random_numbers.add(generate_random_number())

assert len(random_numbers) > 1, "Error: Function should return different numbers on multiple calls"

print("All tests passed successfully!")
