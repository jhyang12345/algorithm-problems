# Given a list of numbers, and a target number n
# find all unique combinations of a, b, c, d, such that a + b + c + d = n.
#
# Here's some examples and some starting code.

def two_sum(arr, target):
    start = 0
    end = len(arr) - 1
    while start < end:
        cur = arr[start] + arr[end]
        if cur < target:
            start += 1
        elif cur > target:
            end -= 1
        else:
            return [arr[start], arr[end]]
    return None


def fourSum(nums, target):
    nums.sort()
    ret = set()
    n = len(nums)
    for i in range(n - 3):
        for j in range(i + 3, n):
            cur_target = nums[i] + nums[j]
            val = two_sum(nums[i + 1:j], - cur_target + target)
            if val:
                ret.add(tuple([nums[i]] + val + [nums[j]]))
    return ret

print(fourSum([1, 1, -1, 0, -2, 1, -1], 0))
# print [[-1, -1, 1, 1], [-2, 0, 1, 1]]

print(fourSum([3, 0, 1, -5, 4, 0, -1], 1))
# print [[-5, -1, 3, 4]]

print(fourSum([0, 0, 0, 0, 0], 0))
# print ([0, 0, 0, 0])
