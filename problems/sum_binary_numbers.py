# Given two binary numbers represented as strings, return the sum of the two binary numbers
# as a new binary represented as a string. Do this without converting the whole binary string into an integer.
#
# Here's an example and some starter code.

def sum_binary(bin1, bin2):
    a = bin1
    b = bin2
    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    else:
        a = '0' * (len(b) - len(a)) + a
    ret = []
    carry = 0
    for i in range(len(a) - 1, -1, -1):
        x = a[i]
        y = b[i]
        num = int(x) + int(y) + carry
        carry = num // 2
        ret.append(str(num % 2))
    if carry != 0:
        ret.append(str(carry))
    return "".join(ret[::-1])




print(sum_binary("11101", "1011"))
# 101000
