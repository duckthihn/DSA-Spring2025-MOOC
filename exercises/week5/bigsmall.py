def count_pairs(numbers):
    numbers = sorted(numbers)
    n = len(numbers)

    count = 0
    left, right = 0, n // 2

    while left < n // 2 and right < n:
        if numbers[right] >= 2 * numbers[left]:
            count += 1
            left += 1
            right += 1
        else:
            right += 1

    return count


if __name__ == "__main__":
    print(count_pairs([1]))  # 0
    print(count_pairs([1, 2, 3]))  # 1
    print(count_pairs([1, 2, 3, 4]))  # 2
    print(count_pairs([1, 1, 1, 1]))  # 0
    print(count_pairs([10 ** 9, 1, 1, 1]))  # 1
    print(count_pairs([4, 5, 1, 4, 7, 8]))  # 2
    print(count_pairs([1, 2, 3, 2, 4, 6]))  # 3

    numbers = [(x * 999983) % 10 ** 6 + 1 for x in range(10 ** 5)]
    print(count_pairs(numbers))  # 41176