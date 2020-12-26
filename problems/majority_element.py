# A majority element is an element that appears more than half the time.
# Given a list with a majority element, find the majority element.
#
# Here's an example and some starting code.

def majority_element(nums):
    dict = {}
    n = len(nums)
    for x in nums:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1
        if dict[x] > n / 2:
            return x
    return None

print(majority_element([3, 5, 3, 3, 2, 4, 3]))
# 3
