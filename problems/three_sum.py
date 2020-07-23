from collections import Counter

# Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that a + b + c = 0.
# Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be duplicates.
# https://leetcode.com/problems/3sum/submissions/
def three_sum(pre_arr):
    counter = Counter(pre_arr)
    nums = []
    for key in counter:
        nums += ([key] * min(3, counter[key]))
    sum_dict = {}
    vals = {}
    for i in range(len(nums)):
        sum_dict[nums[i]] = i
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums)):
            x = nums[i]
            y = nums[j]
            s = -(x + y)
            if s in sum_dict and sum_dict[s] != i and sum_dict[s] != j:
                arr = sorted([x, y, s])
                vals[str(arr)] = arr

    return list(vals.values())

nums = [0, -1, 2, -3, 1]
print(three_sum(nums))

nums = [1, -2, 1, 0, 5]
print(three_sum(nums))
