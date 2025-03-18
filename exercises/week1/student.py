def check_number(number):
    # Str convert to int, and store in list
    nums = [int(digit) for digit in number]

    if nums[0] == 0 and len(nums) == 9:
        weight = [3,7,1,3,7,1,3,7]
        multiply = [a * b for a,b in zip(nums,weight)]
        result  = sum(multiply)
        check_digit = (10 -(result % 10)) % 10
        return check_digit == nums[-1]
    else:
        return False


if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False