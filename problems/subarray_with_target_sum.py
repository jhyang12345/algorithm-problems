# You are given an array of integers, and an integer K. Return the subarray which sums to K.
# You can assume that a solution will always exist.

def find_continuous_k(arr, k):
    start = 0
    end = 1
    cur = arr[0]
    while start < len(arr):
        if cur < k:
            cur += arr[end]
            end += 1
        elif cur > k:
            cur -= arr[start]
            start += 1
        elif start >= end:
            end = start + 1
            cur = arr[start]
        if cur == k:
            return arr[start:end]
    return arr


print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]

print(find_continuous_k([1, 3, 2], 6))
