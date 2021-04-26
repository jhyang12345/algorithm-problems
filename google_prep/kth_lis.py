def kth_lis(arr):
    ret = 1
    n = len(arr)
    cache = [1] * n
    for i in range(n - 1):
        for j in range(i + 1, n):
            if cache[i][j]

# Couldn't solve properly, it's in the book

arr = [5, 1, 6, 4, 3, 2, 8, 7]
