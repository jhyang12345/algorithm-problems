from pprint import pprint
# 4 3
# 1 2 3

def coin_change(coins, s):
    n = len(coins)
    cache = [[0 for _ in range(s + 1)] for __ in range(n + 1)]
    cache[0][0] = 1
    for i in range(n):
        for j in range(s + 1):
            coin = coins[i]
            if j + coin <= s:
                cache[i][j + coin] += cache[i][j]
            cache[i + 1][j] += cache[i][j]
    print("\n".join(list(map(str, cache))))
    return cache[n - 1][s]

def coin_change_2(coins,i, s):
    if s == 0:
        return 1
    elif i < 0 or s < 0:
        return 0
    else:
        return coin_change_2(coins, i - 1, s) + coin_change_2(coins, i, s - coins[i])

coins = [2, 5, 3, 6]
s = 10
print(coin_change(coins, s))
print(coin_change_2(coins, len(coins) - 1, s))