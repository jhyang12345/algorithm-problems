# Given a 32-bit integer, swap the 1st and 2nd bit, 3rd and 4th bit,
# up til the 31st and 32nd bit.
#
# Here's some starting code and an example:

def swap_bits(num):
    i = 0
    ret = 0
    while num > 0:
        r = num % 4
        one = r % 2
        two = r // 2
        s = one * 2 + two
        ret += s * (4 ** i)
        num //= 4
        i += 1
        print(i, num)
    return ret

print(f"0b{swap_bits(0b10101010101010101010101010101010):032b}")
# 0b01010101010101010101010101010101
