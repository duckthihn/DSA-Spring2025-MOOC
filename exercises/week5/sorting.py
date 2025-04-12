# Smallest Difference
def min_diff(nums):
    nums = sorted(nums)

    result = nums[1] - nums[0]
    for i in range(2, len(nums)):
        result = min(result, nums[i] - nums[i-1])

    return result

nums = [4,1,7,3,9]
print(min_diff(nums))

#