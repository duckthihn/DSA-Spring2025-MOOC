import random
import time

numbers = [random.randint(0, 100) for _ in range(10**7)]

# implementation 1
def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# implementation 2
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)

# Measure time for count_even
start_time = time.time()
count1 = count_even(numbers)
end_time = time.time()
print(f"count_even Time: {end_time - start_time:.2f} seconds")

# Measure time for count_even2
start_time = time.time()
count2 = count_even2(numbers)
end_time = time.time()
print(f"count_even2 Time: {end_time - start_time:.2f} seconds")
