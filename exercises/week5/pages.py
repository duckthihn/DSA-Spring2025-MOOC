def create_string(pages):
    if not pages:
        return ""
    # Remove duplicates and sort
    sorted_pages = sorted(list(set(pages)))
    result = ""

    ranges = []
    start = sorted_pages[0]
    prev = start

    for num in sorted_pages[1:]:
        if num == prev + 1:
            prev = num
        else:
            if start == prev:
                ranges.append(f"{start}")
            else:
                ranges.append(f"{start}-{prev}")
            start = num
            prev = num
    # Add the last range or number
    if start == prev:
        ranges.append(f"{start}")
    else:
        ranges.append(f"{start}-{prev}")

    return ",".join(ranges)


if __name__ == "__main__":
    print(create_string([1]))  # 1
    print(create_string([1, 2, 3]))  # 1-3
    print(create_string([1, 1, 1]))  # 1
    print(create_string([1, 2, 1, 2]))  # 1-2
    print(create_string([1, 6, 2, 5]))  # 1-2,5-6
    print(create_string([1, 3, 5, 7]))  # 1,3,5,7
    print(create_string([1, 8, 2, 7, 3, 6, 4, 5]))  # 1-8
    print(create_string([3, 2, 9, 4, 3, 6, 9, 8]))  # 2-4,6,8-9

    pages = [3, 2, 1, 3, 2, 1]
    print(create_string(pages))  # 1-3
    print(pages)  # [3, 2, 1, 3, 2, 1]