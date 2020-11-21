# Given a list of sorted numbers, and two integers k and x, find k closest numbers to the pivot x.
#
# Here's an example and some starter code:

def closest_nums(nums, k, x):
    start = 0
    end = len(nums) - 1
    for i in range(len(nums)):
        cur = nums[i]
        if abs(cur - x) < abs(nums[start] - x):
            start = i
            end = i
    if len(nums) < k:
        return nums
    print(start, end)
    while end - start < k:
        left = None
        right = None
        if start > 0:
            left = nums[start - 1]
        if end < len(nums) - 1:
            right = nums[end + 1]
        if left and right:
            gap_left = abs(x - left)
            gap_right = abs(x - right)
            if gap_left < gap_right:
                start -= 1
            else:
                end += 1
        elif left:
            start -= 1
        elif right:
            end += 1
    return nums[start:end]




print(closest_nums([1, 3, 7, 8, 9], 3, 5))
# [7, 3, 8]


print(closest_nums([1, 3, 5, 7, 8, 9], 3, 5))
