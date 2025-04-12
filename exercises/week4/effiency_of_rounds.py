import time


def count_rounds_dict(numbers):
    n = len(numbers)

    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i

    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    return rounds


def count_rounds(numbers):
    n = len(numbers)
    pos = [0] * (n+1)

    for i in range(n):
        pos[numbers[i]] = i

    rounds = 1
    for number in range(2, n+1):
        if pos[number] < pos[number - 1]:
            rounds += 1

    return rounds


n = 10**7


start_time = time.time()
numbers = list(reversed(range(1, n+1)))
print(count_rounds_dict(numbers))  # 100000
end_add = time.time()

start_time = time.time()
numbers = list(reversed(range(1, n+1)))
print(count_rounds(numbers))  # 100000
end_del = time.time()

print("Dict time:", round(end_add - start_time, 3), "s")
print("List time:", round(end_del - end_add, 3), "s")