def edit_distance(a, b):
    n = len(a)
    m = len(b)
    cache = [[-1 for _ in range(m + 1)] for __ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                cache[i][j] = 0
            else:
                cur_min = min(cache[i][j - 1] + 1, cache[i - 1][j] + 1)
                if a[i - 1] == b[j - 1]:
                    cur_min = cache[i - 1][j - 1]
                else:
                    cur_min = cache[i - 1][j - 1] + 1
                cache[i][j] = cur_min
    return cache[n][m]

print(edit_distance('biting', 'sitting'))
print(edit_distance('abc', 'abf'))
