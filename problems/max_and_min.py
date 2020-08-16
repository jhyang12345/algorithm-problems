# Given a list of numbers of size n, where n is greater than 3,
# find the maximum and minimum of the list using less than 2 * (n - 1) comparisons.
#
# Here's a start:

def find_min_max(nums):
    cur_max = nums[0]
    cur_min = nums[0]
    for x in nums[1:]:
        if cur_max < x:
            cur_max = x
        if cur_min > x:
            cur_min = x
    return cur_min, cur_max

print(find_min_max([3, 5, 1, 2, 4, 8]))
