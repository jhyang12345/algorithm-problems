# Given a list of numbers and a target number,
# find all possible unique subsets of the list of
# numbers that sum up to the target number. The numbers will all be positive numbers.
#
# Here's an example and some starter code.

def get_target(nums, target):
    ret = [] # list of lists
    if target == 0:
        return []
    for i in range(len(nums)):
        possibilities = get_target(nums[i + 1:], target - nums[i])
    return ret

def sum_combinations(nums, target):
    ret = []
    nums.sort()


print(sum_combinations([10, 1, 2, 7, 6, 1, 5], 8))
# [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]
