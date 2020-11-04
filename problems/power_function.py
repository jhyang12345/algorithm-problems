# The power function calculates x raised to the nth power.
# If implemented in O(n) it would simply be a for loop over
# n and multiply x n times. Instead implement this power
# function in O(log n) time. You can assume that n will be a non-negative integer.
#
# Here's some starting code:

def pow(x, n):
    if n == 1:
        return x
    elif n == 0:
        return 1
    return pow(x, n // 2) * pow(x, n - n // 2)

print(pow(5, 3))
# 125



print(pow(2, 10))
# 125
