# You are given an array of integers. Return the length of the longest increasing
# subsequence (not necessarily contiguous) in the array.

# Example:
# [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

def lis(arr):
    n = len(arr)
    cache = [1] * n
    ret = 1
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                cache[i] = max(cache[i], cache[j] + 1)
                ret = max(ret, cache[i])
    print(cache)
    return ret

arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(lis(arr))
