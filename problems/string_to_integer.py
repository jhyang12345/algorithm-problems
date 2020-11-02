# Given a string, convert it to an integer without using the builtin str function.
# You are allowed to use ord to convert a character to ASCII code.
#
# Consider all possible cases of an integer. In the case where the string is not a
# valid integer, return None.
#
# Here's some starting code:

def get_num(num):
    ret = 0
    i = 0
    for x in num[::-1]:
        ret += int(x) * (10 ** i)
        i += 1
    return ret


def convert_to_int(s):
    s = s.strip()
    if not s:
        return None
    for ch in s:
        if ch not in '-1234567890':
            return None
    if s[0] == '-':
        return - get_num(s[1:])
    else:
        return get_num(s[1:])

print(convert_to_int('-105') + 1)
# -104
