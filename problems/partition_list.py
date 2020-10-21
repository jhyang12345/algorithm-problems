# Given a list of numbers and an integer k, partition/sort
# the list such that the all numbers less than k occur before k,
# and all numbers greater than k occur after the number k.

def partition_list(nums, k):
    left = []
    exact = []
    right = []
    for x in nums:
        if x < k:
            left.append(x)
        elif x > k:
            right.append(x)
        else:
            exact.append(x)
    return left + exact + right

print(partition_list([2, 2, 2, 5, 2, 2, 2, 2, 5], 3))
# [2, 2, 2, 2, 2, 2, 2, 2, 5]
