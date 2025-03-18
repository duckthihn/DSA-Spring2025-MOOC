def find_rounds(numbers):
    n = len(numbers)
    rounds = []

    next_expected = 1

    while next_expected <= n:
        collected = []

        for num in numbers:
            if num == next_expected:
                collected.append(num)
                next_expected += 1
        rounds.append(collected)
    return rounds


if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]

    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]