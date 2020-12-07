# Given a list of numbers and a target number n, find 3 numbers
# in the list that sums closest to the target number n.
# There may be multiple ways of creating the sum closest to the
# target number, you can return any combination in any order.
#
# Here's an example and some starter code.
# https://www.geeksforgeeks.org/find-a-triplet-in-an-array-whose-sum-is-closest-to-a-given-number/

def closest_3sum(nums, target):
    nums.sort()
    n = len(nums)
    closest = None
    ret = []
    for i in range(n - 2):
        start = i + 1
        end = n - 1
        while start < end:
            cur_sum = nums[i] + nums[start] + nums[end]
            if closest == None or abs(target - cur_sum) < abs(target - closest):
                closest = cur_sum
                ret = [nums[i], nums[start], nums[end]]
            if cur_sum > target:
                end -= 1
            else:
                start += 1
    return ret, closest


print(closest_3sum([2, 1, -5, 4], -1))
# Closest sum is -5+1+2 = -2 OR -5+1+4 = 0
# print [-5, 1, 2]
