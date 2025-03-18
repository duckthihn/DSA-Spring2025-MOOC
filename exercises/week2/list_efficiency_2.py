import time

n = 10 ** 5

ls = []

# Measure additions time
start_time = time.time()
for i in range(1, n + 1):
    ls.append(i)
print(f"{time.time() - start_time} seconds")

# Measure deletions time
start_time = time.time()
for _ in range(n):
    ls.pop(0) # delete first element

print(f"{time.time() - start_time} seconds")