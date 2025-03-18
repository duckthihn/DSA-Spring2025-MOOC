def binary_gap(N):
    # Implement your solution here
    num = bin(N)[2:]
    count = 0
    max_count = 0
    print(num)

    for digit in num:
        if digit == "0":
            count += 1
        elif digit == "1":
            max_count = max(count, max_count)
            count = 0

    return max_count