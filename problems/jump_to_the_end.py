# Starting at index 0, for an element n at index i, you are allowed to jump at most n indexes ahead.
# Given a list of numbers, find the minimum number of jumps to reach the end of the list.
#
# Example:
# Input: [3, 2, 5, 1, 1, 9, 3, 4]
# Output: 2
# Explanation:
#
# The minimum number of jumps to get to the end of the list is 2:
# 3 -> 5 -> 4

# https://leetcode.com/problems/jump-game-ii/discuss/774616/Easy!-Linear-Time-O(n)-and-Space-O(1)-oror-Explanation


def jumpToEnd(nums):
    n = len(nums)
    cache = [i for i in range(n)]
    for i in range(n):
        step = nums[i]
        for x in range(1, step + 1):
            if i + x < n:
                cache[i + x] = min(cache[i + x], cache[i] + 1)
                if i + x == n -1:
                    return cache[i + x]
            else:
                break
    return cache[n - 1]

print(jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))

print(jumpToEnd([2,3,1,1,4]))
