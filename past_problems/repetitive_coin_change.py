coins = [1, 2, 3]
s = 4

def coin_change_repeat(coins, s):
    cache = [0 for _ in range(s + 1)]
    cache[0] = 1
    for i in range(s):
        for coin in coins:
            if i + coin <= s:
                cache[i + coin] += cache[i]
    return cache[s]


print(coin_change_repeat(coins, s))