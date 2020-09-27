# A fixed point in a list is where the value is equal to its index.
# So for example the list [-5, 1, 3, 4], 1 is a fixed point in the list
# since the index and value is the same. Find a fixed point
# (there can be many, just return 1) in a sorted list of distinct elements, or return None if it doesn't exist.
#
# Here is a starting point:

def find_fixed_point(nums):
    hi = len(nums)
    lo = 0
    mid = (hi + lo) // 2
    while True:
        cur = nums[mid]
        if cur > mid:
            hi = mid
        elif cur < mid:
            lo = mid
        else:
            return mid
        mid = (hi + lo) // 2

print(find_fixed_point([-5, 1, 3, 4]))
# 1
