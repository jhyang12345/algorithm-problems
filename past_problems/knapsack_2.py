value = [60, 100, 120]
weights = [10, 20, 30]
space = 50

def knapsack(values, weights, space):
    n = len(values)
    cache = [[0 for _ in range(space + 1)] for __ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, space + 1):
            value = values[i - 1]
            weight = weights[i - 1]
            cache[i][j] = max(cache[i - 1][j], cache[i][j])
            if j >= weight:
                cache[i][j] = max(cache[i][j], cache[i - 1][j - weight] + value)
    return cache[n][space]

print(knapsack(value, weights, space))