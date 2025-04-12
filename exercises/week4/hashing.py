def hash_value(string):
    A = 23
    M = 2**32
    hash_val = 0

    for i, char in enumerate(string):
        char_val = ord(char) - ord("a")
        power = len(string) - i - 1
        hash_val += (char_val * A**power)

    return hash_val % M

if __name__ == "__main__":
    print(hash_value("abc")) # 25
    print(hash_value("kissa")) # 2905682
    print(hash_value("aybabtu")) # 154753059
    print(hash_value("tira")) # 235796
    print(hash_value("zzzzzzzzzz")) # 2739360440