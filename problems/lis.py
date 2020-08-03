def lis(arr):
    n = len(arr)
    if not n:
        return n
    cache = [1 for _ in range(n+1)]
    ret = 1
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                cache[i] = max(cache[i], cache[j] + 1)
                ret = max(cache[i], ret)
    return ret


print(lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
