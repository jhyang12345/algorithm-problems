# Given a number n, find the least number of squares needed to sum up to the number.
#
# Here's an example and some starting code:

def calc_sum(n, cache):
    if n == 0:
        return 0
    if cache[n] != -1:
        return cache[n]
    ret = -1
    for i in range(1, n + 1):
        value = 0
        leftover = n - (i ** 2)
        if leftover < 0:
            break
        value = calc_sum(leftover, cache) + 1
        if ret == -1 or value < ret:
            ret = value
    return ret


def square_sum(n):
    cache = [-1] * (n + 1)
    return calc_sum(n, cache)



print(square_sum(13))
# Min sum is 32 + 22
# 2



print(square_sum(1))
# Min sum is 32 + 22
# 2



print(square_sum(12))
# Min sum is 32 + 22
# 2
