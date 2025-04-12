def create_distribution(string):
    substrings = set()
    n = len(string)

    for i in range(n):
        for j in range(i, n):
            substrings.add(string[i:j + 1])

    distribution = {}
    for substring in substrings:
        length = len(substring)
        if length not in distribution:
            distribution[length] = 0
        distribution[length] += 1

    return distribution


if __name__ == "__main__":
    print(create_distribution("aaaa"))
    # {1: 1, 2: 1, 3: 1, 4: 1}

    print(create_distribution("abab"))
    # {1: 2, 2: 2, 3: 2, 4: 1}

    print(create_distribution("abcd"))
    # {1: 4, 2: 3, 3: 2, 4: 1}

    print(create_distribution("abbbbbb"))
    # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 1}

    print(create_distribution("aybabtu"))
    # {1: 5, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}