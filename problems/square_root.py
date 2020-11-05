# Given a positive integer, find the square root of the integer
# without using any built in square root or
# power functions (math.sqrt or the ** operator). Give accuracy up to 3 decimal points.
#
# Here's an example and some starter code:

def sqrt(x):
    lo = 0
    hi = x
    count = 0
    while count < 1000:
        mid = (hi + lo) / 2
        if mid * mid < x:
            lo = mid
        else:
            hi = mid
        count += 1
    return mid

print(sqrt(5))
# 2.236
