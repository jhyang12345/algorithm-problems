# Given an array and an integer k, rotate the array by k spaces.
# Do this without generating a new array and without using extra space.
#
# Here's an example and some starter code

def rotate_list(nums, k):
    n = len(nums)
    move = k % n
    for i in range(move):
        c = nums[0]
        for j in range(n):
            if j == n - 1:
                nums[j] = c
            else:
                nums[j] = nums[j + 1]
    


a = [1, 2, 3, 4, 5]
rotate_list(a, 2)
print(a)
# [3, 4, 5, 1, 2]
