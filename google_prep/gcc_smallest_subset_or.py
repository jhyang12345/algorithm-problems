# Given an array of positive integers. The task is to find the size of
# the smallest subset such that the Bitwise OR of that set is Maximum possible.
from pprint import pprint
def smallest_subset(arr):
    max_sum = 0
    for x in arr:
        max_sum = max_sum | x
    n = len(arr)
    cache = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
    cur_min = n
    for x in range(1, n + 1):
        i = x - 1
        cur = arr[i]
        for y in range(x):
            cache[x][y + 1] = max(cache[x - 1][y] | cur, cache[x - 1][y + 1])
            if cache[x][y + 1] == max_sum:
                cur_min = min(cur_min, y + 1)
    return cur_min

arr = [5, 1, 3, 4, 2]

print(smallest_subset(arr))

arr = [2, 6, 2, 8, 4, 5]

print(smallest_subset(arr))
