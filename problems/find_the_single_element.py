# Given an array of integers, arr, where all numbers occur twice except one number which occurs once, find the number. 
# Your solution should ideally be O(n) time and use constant extra

def findSingle(nums):
    ret = 0
    for x in nums:
        ret ^= x
    return ret


nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(findSingle(nums))

print(findSingle([7, 3, 5, 5, 4, 3, 4, 8, 8]))
