# Given a list of possible coins in cents, and an amount (in cents) n,
# return the minimum number of coins needed to create the amount n.
# If it is not possible to create the amount using the given coin denomination, return None.
#
# Here's an example and some starter code:

def make_change(coins, n):
    cache = [-1] * (n + 1)
    cache[0] = 0
    for i in range(n):
        for coin in coins:
            if cache[i] != -1:
                if i + coin <= n:
                    if cache[i + coin] == -1:
                        cache[i + coin] = cache[i] + 1
                    else:
                        cache[i + coin] = min(cache[i + coin], cache[i] + 1)
    return cache[n]




print(make_change([1, 5, 10, 25], 36))
# 3 coins (25 + 10 + 1)
