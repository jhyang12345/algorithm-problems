# Given a numerator and a denominator, find what the equivalent decimal representation is as a string.
# If the decimal representation has recurring digits, then put those digits in brackets
# (ie 4/3 should be represented by 1.(3) to represent 1.333...). Do not use any built in
# evaluator functions like python's eval. You can also assume that the denominator will be nonzero.
#
# Here's some examples and some starter code:

def frac_to_dec(numerator, denominator):
    ret = ''
    number = numerator
    if denominator * numerator < 0:
        ret += '-'
        number = - numerator
    numerator = abs(numerator)
    denominator = abs(denominator)
    repeat = False
    value = 1
    last = value
    i = 0
    while True:
        if number == 0:
            break
        if value >= 10 and '.' not in ret:
            ret += '.'
        if (number * value) > denominator:
            ret = ret + str(int((number * value) // denominator))
            if number == (number * value) % denominator and value == last:
                repeat = True
                break
            number = (number * value) % denominator
            last = value
            value = 1
        else:
            ret = ret + '0'
        value *= 10

        i += 1
        if i > 10:
            break
    if not repeat:
        return ret
    digits = len(str(last)) - 1
    expr = str(int((number * last) // denominator))
    while len(expr) < digits:
        expr = '0' + expr

    i = len(ret) - len(expr)
    step = len(expr)
    while i >= 0:
        if ret[i:i + step] != expr:
            i = i + step
            break
        i -= step
    return ret[:i] + f"({expr})"


print(frac_to_dec(-3, 2))
# -1.5

print(frac_to_dec(4, 3))
# 1.(3)

print(frac_to_dec(1, 6))
# 0.1(6)

print(frac_to_dec(1, 11))
