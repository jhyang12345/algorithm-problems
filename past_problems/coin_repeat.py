s = 4
coins = [1, 2, 3]

def coin_repeat(s, coins):
    cache = [0 for _ in range(s + 1)]
    cache[0] = 1
    for i in range(s + 1):
        for coin in coins:
            if i + coin <= s:
                cache[i + coin] += cache[i]
    return cache[s]

print(coin_repeat(s, coins))