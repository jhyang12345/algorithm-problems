
a = "123456"
b = "35"

def lcs(a, b):
    n = len(a)
    m = len(b)
    cache = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1,m + 1):
            if a[i - 1] == b[j - 1]:
                cache[i][j] = max(cache[i - 1][j - 1] + 1, cache[i][j - 1], cache[i - 1][j])
            else:
                cache[i][j] = max(cache[i][j - 1], cache[i - 1][j])
    return cache[n][m]


print(lcs(a, b))
