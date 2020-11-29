# Given a non-negative integer n, convert the integer to hexadecimal and return the result as a string.
# Hexadecimal is a base 16 representation of a number, where the digits are 0123456789ABCDEF.
# Do not use any builtin base conversion functions like hex.
#
# Here's an example and some starter code.

dict = '0123456789ABCDEF'

def to_hex(n):
    ret = []
    while n:
        index = n % 16
        ret.append(index)
        n = n // 16
    ret = ret[::-1]
    hex = ""
    for i in ret:
        hex += dict[i]
    return hex

print(to_hex(123))
# 7B
