def count_sublists(numbers):
    count = 1
    total = 1

    for i in range(1,len(numbers)):
        if numbers[i] > numbers[i-1]:
            count += 1
        else:
            count = 1

        total += count

    return total


if __name__ == "__main__":
    print(count_sublists([2, 1, 3, 4])) # 7
    print(count_sublists([1, 2, 3, 4])) # 10
    print(count_sublists([4, 3, 2, 1])) # 4
    print(count_sublists([1, 1, 1, 1])) # 4
    print(count_sublists([1, 2, 1, 2])) # 6

    # numbers = list(range(1, 10**5+1))
    # print(count_sublists(numbers)) # 5000050000