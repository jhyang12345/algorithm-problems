from pprint import pprint

a = "123456"
b = "245"

# lcs(i, j ) = max(lcs(i - 1, j), lcs(i, j - 1), lcs(i - 1, j - 1) + 1)
def lcs(a, b):
    n = len(a)
    m = len(b)
    cache = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
    ret = 0
    for i in range(n):
        for j in range(m):
            x = a[i]
            y = b[j]
            if x == y:
                cache[i + 1][j + 1] = max(cache[i + 1][j + 1], cache[i][j] + 1)
            else:
                cache[i + 1][j + 1] = max(cache[i + 1][j + 1], cache[i][j])
            cache[i + 1][j] = max(cache[i + 1][j], cache[i][j])
            cache[i][j + 1] = max(cache[i][j + 1], cache[i][j])
    print("\n".join(list(map(str, cache))))
    return cache[n][m]

def lcs_2(a, b):
    n = len(a)
    m = len(b)
    cache = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            x = a[i - 1]
            y = b[j - 1]
            ret = 0
            if x == y:
                ret = max(ret, cache[i-1][j-1] + 1)
            ret = max(ret, cache[i - 1][j], cache[i][j - 1])
            cache[i][j] = max(cache[i][j], ret)
    return cache[n][m]

print(lcs(a, b))
print(lcs_2(a, b))