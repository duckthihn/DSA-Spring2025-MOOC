def count_rounds(numbers):
    positions = [0] * (len(numbers) + 1)

    for i in range(len(numbers)):
        positions[numbers[i]] = i

    print(positions)
    rounds = []

    small_round = [1]

    for i in range(2, len(numbers) + 1):
        if positions[i] > positions[i - 1]:
            small_round.append(i)
        else:
            rounds.append(small_round)
            small_round = [i]
    rounds.append(small_round)

    return len(rounds)

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