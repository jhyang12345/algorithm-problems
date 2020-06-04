a = "sunday"
b = "saturday"

def edit_distance(a, b):
    n = len(a)
    m = len(b)
    cache = [[-1 for _ in range(m + 1)] for __ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                cache[i][j] = j
            elif j == 0:
                cache[i][j] = i
            else:
                x = a[i - 1]
                y = b[j - 1]
                cache[i][j] = min(cache[i][j - 1], cache[i - 1][j], cache[i - 1][j - 1]) + 1
                if x == y:
                    cache[i][j] = min(cache[i][j], cache[i - 1][j - 1])
    return cache[n][m]
                

print(edit_distance(a, b))