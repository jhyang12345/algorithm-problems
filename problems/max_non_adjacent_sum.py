# Given a list of positive numbers, find the largest possible
# set such that no elements are adjacent numbers of each other.
#
# Here's some example and some starter code

def maxNonAdjacentSum(nums):
    n = len(nums)
    cache = [[0 for i in range(2)] for _ in range(n)]
    cache[0][0] = 0
    cache[0][1] = nums[0]
    ret = 0
    for i in range(1, n):
        cache[i][0] = max(cache[i - 1][1], cache[i - 1][0])
        cache[i][1] = cache[i - 1][0] + nums[i]
        ret = max(ret, cache[i][0], cache[i][1])
    return ret

print(maxNonAdjacentSum([3, 4, 1, 1]))
# 5
# max sum is 4 (index 1) + 1 (index 3)

print(maxNonAdjacentSum([2, 1, 2, 7, 3]))
# 9
# max sum is 2 (index 0) + 7 (index 3)
