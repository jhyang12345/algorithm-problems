# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.


# [1, 2, 0]

# def sortColors( nums):
#     end_0 = 0
#     end_1 = 0
#     start_2 = len(nums) - 1
#     i = 0
#     # while i <= start_2:
#     for i in range(len(nums)):
#         x = nums[i]
#         if i > start_2:
#             break
#         if x == 0:
#             nums[i] = nums[end_0]
#             nums[end_0] = x
#             end_0 += 1
#             end_1 += 1
#             i += 1
#         elif x == 1:
#             nums[i] = nums[end_1]
#             nums[end_1] = x
#             end_1 += 1
#             i += 1
#         elif x == 2:
#             while nums[start_2] == 2:
#                 start_2 -= 2
#             nums[i] = nums[start_2]
#             nums[start_2] = x
#             start_2 -= 1
#         print(x, end_0, end_1, start_2)

def sortColors( nums):
    lo = 0
    mid = 0
    hi = len(nums) - 1
    while mid <= hi:
        cur = nums[mid]
        if cur == 0:
            nums[mid] = nums[lo]
            nums[lo] = cur
            lo += 1
            mid += 1
        elif cur == 1:
            mid += 1
        else:
            nums[mid] = nums[hi]
            nums[hi] = cur
            hi -= 1


nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]


def sort012( a, arr_size):
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi = hi - 1
    return a


# Driver Program
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr_size = len(arr)
arr = sort012( arr, arr_size)

print(arr)
