# Given a sorted list of positive numbers, find the smallest positive number that cannot be a sum of any subset in the list.
#
# Example:
# Input: [1, 2, 3, 8, 9, 10]
# Output: 7
# Numbers 1 to 6 can all be summed by a subset of the list of numbers, but 7 cannot.

def findSmallest(nums):
    ret = nums[0]
    for x in nums[1:]:
        diff = x - ret
        if diff > 1:
            return ret + 1
        else:
            ret += x
    return ret + 1



print(findSmallest([1, 2, 3, 8, 9, 10]))
print(findSmallest([1, 3, 6, 10, 11, 15]))
print(findSmallest([1, 1, 1, 1]))
print(findSmallest([1, 1, 3, 4]))
print(findSmallest([1, 2, 3, 4, 5, 6]))
