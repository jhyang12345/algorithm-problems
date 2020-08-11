# Given a string with a certain rule: k[string] should be expanded to string k times. 
# So for example, 3[abc] should be expanded to abcabcabc.
# Nested expansions can happen, so 2[a2[b]c] should be expanded to abbcabbc.

def decodeString(s):
    ret = ""
    start = -1
    num = 1
    stack = []
    expr_start = -1
    print(s)
    for i in range(len(s)):
        x = s[i]
        if x in '1234567890':
            if start == -1:
                start = i
        elif x == '[':
            stack.append(x)
            if expr_start == -1:
                num = int(s[start:i])
                expr_start = i + 1
        elif x == ']':
            stack.pop()
            if not stack:
                ret += (num * decodeString(s[expr_start:i]))
                start = -1
                expr_start = -1
                num = 1
        else:
            if start == -1:
                ret += x
    return ret



print(decodeString('2[a2[b]c]'))
# abbcabbc
