# Given two arrays, write a function to compute their intersection - the intersection means the numbers that are in both arrays.
#
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:
# Each element in the result must be unique.
# The result can be in any order.


def intersection(nums1, nums2):
    dict_x = {}
    ret = []
    for x in nums1:
        dict_x[x] = 0
    dict_y = {}
    for y in nums2:
        dict_y[y] = 0
    for y in dict_y.keys():
        if y in dict_x:
            ret.append(y)
    return ret

print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
