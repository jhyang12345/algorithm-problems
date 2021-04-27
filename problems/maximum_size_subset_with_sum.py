# This is an extended version of the subset sum problem.
# Here we need to find the size of the maximum size subset
# whose sum is equal to the given sum.
from pprint import pprint

# def max_subset_with_sum(arr, s):
#     n = len(arr)
#     cache = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
#     ret = 0
#     for x in range(1, n + 1):
#         cur = arr[x - 1]
#         for y in range(x):
#             if cache[x - 1][y] <= s - cur:
#                 if cache[x - 1][y] != 0 or y == 0:
#                     cache[x][y + 1] = cache[x - 1][y] + cur
#
#             else:
#                 cache[x][y] = max(cache[x - 1][y], cache[x]
#             if cache[x][y + 1] == s:
#                 ret = max(ret, y + 1)
#     pprint(cache)
#     return ret

def max_subset_with_sum(arr, s):
    n = len(arr)
    cache = [[0 for _ in range(s + 1)] for __ in range(n + 1)]
    cache[0][0] = 0
    for i in range(1, n):
        cur = arr[i - 1]
        for j in range(s + 1):
            if j == 0:
                cache[i][j] = 0
            if cache[i][j] != -1:
                if j + cur <= s:
                    cache[i + 1][j + cur] = max(cache[i][j] + 1, cache[i][j + cur])
                cache[i + 1][j] = max(cache[i + 1][j], cache[i][j])
    return cache[n][s]


arr = [2, 3, 5, 7, 10, 15]
print(max_subset_with_sum(arr, 10))

arr = [1, 2, 3, 4, 5]
print(max_subset_with_sum(arr, 4))
