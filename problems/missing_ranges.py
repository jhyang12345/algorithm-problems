# Given a sorted list of numbers, and two integers low and high representing the
# lower and upper bound of a range, return a list of (inclusive) ranges where the
# numbers are missing. A range should be represented by a tuple in the format of (lower, upper).
#
# Here's an example and some starting code:

def missing_ranges(nums, low, high):
    start = low
    ret = []
    for i, x in enumerate(nums):
        if x > start:
            ret.append((start, x - 1))
            start = x + 1
        if x == start:
            start = x + 1
        if i == (len(nums) - 1):
            if x + 1 <= high:
                ret.append((x + 1, high))
    return ret


print(missing_ranges([1, 3, 5, 10], 1, 10))
# [(2, 2), (4, 4), (6, 9)]
