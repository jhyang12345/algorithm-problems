value = [60, 100, 120]
weights = [10, 20, 30]
space = 50

def knapsack(values, weights, space):
    n = len(values)
    cache = [[0 for _ in range(space + 1)] for __ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(space + 1):
            value = values[i - 1]
            weight = weights[i - 1]
            if j - weight >= 0:
                cache[i][j] = max(cache[i - 1][j], cache[i - 1][j - weight] + value)
            else:
                cache[i][j] = cache[i - 1][j]
    print(cache)
    return cache[n][space]

def knapsack_2(values, weights, space):
    n = len(values)
    cache = [[0 for _ in range(space + 1)] for __ in range(n + 1)]
    for i in range(n):
        for j in range(space + 1):
            value = values[i]
            weight = weights[i]
            if j + weight <= space:
                cache[i + 1][j + weight] = max(cache[i][j] + value, cache[i + 1][j + weight])
            cache[i + 1][j] = max(cache[i + 1][j], cache[i][j])
    print(cache)
    return cache[n][space]

print(knapsack(value, weights, space))
print(knapsack_2(value, weights, space))