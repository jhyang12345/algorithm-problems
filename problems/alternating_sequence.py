arr = [4, 8, 2, 5, 6, 8]

def alternating(arr):
    n = len(arr)
    cache = [[0, 0] for _ in range(n)]
    ret = 0
    for i in range(n):
        cur = arr[i]
        cache[i][0] = max(cur, cache[i][0])
        cache[i][1] = max(cur, cache[i][1])
        for j in range(i + 1, n):
            next = arr[j]
            if cache[i][1] == cur and next < cur:
                cache[j][0] = max(cache[j][0], cache[i][1] + next)
            if cache[i][0] >= cur and next > cur:
                cache[j][1] = max(cache[j][1], cache[i][0] + next)
            ret = max(ret, max(cache[j]))
            
    return ret

print(alternating(arr))