# Given an integer, reverse the digits. Do not convert the integer into a string and reverse it.
#
# Here's some examples and some starter code.

def reverse_integer(num):
    buffer = abs(num)
    stack = []
    while buffer:
        leftover = buffer % 10
        buffer = buffer // 10
        stack.append(leftover)
    value = 0
    i = 0
    while stack:
        cur = stack.pop()
        value += (cur * (10 ** i))
        i += 1
    if num < 0:
        return - value
    else:
        return value

print(reverse_integer(135))
# 531

print(reverse_integer(-321))
# -123
