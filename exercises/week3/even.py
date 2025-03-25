def count_sublists(numbers):
    count = 0
    total_sublists = 0

    for num in numbers:
        if num % 2 == 0:
            count += 1
        else:
            total_sublists += (count * (count + 1)) // 2
            count = 0

    total_sublists += (count * (count + 1)) // 2
    return total_sublists


if __name__ == "__main__":
    print(count_sublists([2, 4, 1, 6])) # 4
    print(count_sublists([1, 2, 3, 4])) # 2
    print(count_sublists([1, 1, 1, 1])) # 0
    print(count_sublists([2, 2, 2, 2])) # 10
    print(count_sublists([1, 1, 2, 1])) # 1

    numbers = [2] * 10**5
    print(count_sublists(numbers)) # 5000050000