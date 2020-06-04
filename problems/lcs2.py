a = "123456"
b = "245"

def lcs(a, b):
    n = len(a)
    m = len(b)
    cache = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            x = a[i - 1]
            y = b[j - 1]
            if x == y:
                cache[i][j] = max(cache[i][j], cache[i - 1][j - 1] + 1)
            cache[i][j] = max(cache[i][j], cache[i - 1][j], cache[i][j - 1])
    return cache[n][m]

print(lcs(a, b))