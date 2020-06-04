s = 10
coins = [2, 3, 5, 6]

def coin_change(s, coins):
    n = len(coins)
    cache = [[0 for _ in range(s + 1)] for __ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(s + 1):
            if j == 0:
                cache[i][j] = 1
            else:
                coin = coins[i - 1]
                if j >= coin:
                    cache[i][j] += cache[i][j - coin]
                cache[i][j] += cache[i - 1][j]
    return cache[n][s]

print(coin_change(s, coins))