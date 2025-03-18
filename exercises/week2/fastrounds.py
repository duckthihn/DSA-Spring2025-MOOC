def count_rounds(numbers):
    rounds = 1
    current_max = numbers[0]

    for num in numbers[1:]:
        if num < current_max:
            rounds += 1
        current_max = max(current_max, num)

    return rounds


if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4]))  # 1
    print(count_rounds([1, 3, 2, 4]))  # 2
    print(count_rounds([4, 3, 2, 1]))  # 4
    print(count_rounds([1]))  # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8]))  # 4

    n = 10 ** 5
    numbers = list(reversed(range(1, n + 1)))
    print(count_rounds(numbers))  # 100000
    print(count_rounds([2, 5, 4, 1, 3])) # 4