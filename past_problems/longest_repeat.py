text = "aaabbbbcccccdd"

def longest(text):
    if len(text) <= 0:
        return 0
    cur = text[0]
    ret = 1
    cur_max = ret
    for ch in text[1:]:
        if ch == cur:
            ret += 1
        else:
            cur = ch
            ret = 1
        cur_max = max(cur_max, ret)
    return cur_max

print(longest(text))