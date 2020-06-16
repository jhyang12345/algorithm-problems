# You are given a positive integer N which represents the number of steps in a staircase.
# You can either climb 1 or 2 steps at a time. Write a function that returns the number
# of unique ways to climb the stairs.

def staircase(n):
    cache = [0] * (n + 1)
    cache[0] = 1
    for x in range(1, n + 1):
        value = 0
        if x >= 1:
            value += cache[x - 1]
        if x >= 2:
            value += cache[x - 2]
        cache[x] = value
    return cache[n]


print(staircase(4))
# 5
print(staircase(5))
