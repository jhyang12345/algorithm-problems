def lis(arr):
    n = len(arr)
    cache = [1] * (n + 1)
    ret = 1
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                cache[j] = max(cache[j], cache[i] + 1)
            ret = max(ret, cache[j])
    return ret


print(lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
