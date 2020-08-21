# Given a string, rearrange the string so that no character next to each other are the same.
# If no such arrangement is possible, then return None.
#
# Example:
# Input: abbccc
# Output: cbcbca
def rearrangeString(s):
    chars = {}
    n = len(s)
    for ch in s:
        if ch not in chars:
            chars[ch] = 1
        else:
            chars[ch] += 1
    arr = list(chars.keys())
    ret = ""
    while True:
        next = None
        max_count = 0
        for ch in chars:
            if len(ret) > 0 and  ch == ret[-1] or chars[ch] == 0:
                continue
            else:
                if chars[ch] > max_count:
                    max_count = chars[ch]
                    next = ch
        if next == None:
            break
        else:
            ret += next
            chars[next] -= 1
    if n != len(ret):
        return False
    return ret


print(rearrangeString('abbccc'))

print(rearrangeString('abbb'))

print(rearrangeString('abb'))
