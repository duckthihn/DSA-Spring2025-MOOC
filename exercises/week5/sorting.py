# Smallest Difference
def min_diff(nums):
    nums = sorted(nums)

    result = nums[1] - nums[0]
    for i in range(2, len(nums)):
        result = min(result, nums[i] - nums[i-1])

    return result

nums = [4,1,7,3,9]
print(min_diff(nums))

# Restaurant
def max_customers(arrivals, departures):
    events = []
    for time in arrivals:
        events.append((time, 1))
    for time in departures:
        events.append((time, 2))

    events.sort()

    counter = 0
    result = 0
    for event in events:
        if event[1] == 1:
            counter += 1
        if event[1] == 2:
            counter -= 1
        result = max(result, counter)

    return result
