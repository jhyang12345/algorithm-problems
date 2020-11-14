# Given a non-negative integer n, convert n to base 2 in string form.
# Do not use any built in base 2 conversion functions like bin.
#
# Here's an example and some starter code:

def base_2(n):
    ret = ''
    while n:
        remainder = n % 2
        ret += str(remainder)
        n //= 2
    return ret[::-1]

print(base_2(123))
# 1111011
