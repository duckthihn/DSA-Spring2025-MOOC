def find_sums(numbers, size):
    # condition
    if size > len(numbers) or size <= 0:
        return []

    result = []
    # # sliding windows
    window_sum = sum(numbers[:size]) # compute sum of the first window
    result.append(window_sum)

    for i in range(len(numbers) - size):
        window_sum += numbers[i + size] - numbers[i]
        result.append(window_sum)

    return result


if __name__ == "__main__":
    print(find_sums([1], 1)) # [1]
    print(find_sums([1, 8, 2, 7, 3, 6, 4, 5], 6)) # [27, 30, 27]

    print(find_sums([1, 2, 3, 4, 5], 1)) # [1, 2, 3, 4, 5]
    print(find_sums([1, 2, 3, 4, 5], 2)) # [3, 5, 7, 9]
    print(find_sums([1, 2, 3, 4, 5], 3)) # [6, 9, 12]
    print(find_sums([1, 2, 3, 4, 5], 4)) # [10, 14]
    print(find_sums([1, 2, 3, 4, 5], 5)) # [15]

    # numbers = list(range(10**5))
    # sums = find_sums(numbers, 10**4)
    # print(sums[5]) # 50045000
    # print(sums[42]) # 50415000
    # print(sums[1337]) # 63365000