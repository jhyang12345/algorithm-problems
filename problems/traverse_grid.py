def num_ways(n, m):
    cache = [[0 for _ in range(m)] for __ in range(n)]
    cache[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                cache[i][j] = 1
            else:
                cache[i][j] = cache[i][j - 1] + cache[i - 1][j]
    return cache[n - 1][m - 1]

print(num_ways(2, 2))
print(num_ways(3, 3))
print(num_ways(4, 4))
