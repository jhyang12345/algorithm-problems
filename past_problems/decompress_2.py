text = "3[abc]4[ab]c"
numbers = "1234567890"
alphas = "abcdefghijklmnopqrstuvwxyz"

def decompress(text):
    num = ""
    exp_started = False
    start = -1
    end = -1
    q = []
    ret = ""
    for i, ch in enumerate(text):
        if ch in numbers:
            exp_started = True
            if start == -1:
                num += ch
        elif ch == "[":
            if start == -1:
                start = i + 1
            q.append(ch)
        elif ch == "]": 
            q.pop()
            if len(q) == 0:
                end = i
                ret += decompress(text[start:end]) * int(num)
                num = ""
                exp_started = False
                start = -1
                end = -1
        elif ch in alphas and not exp_started:
            ret += ch
    return ret

print(decompress(text))
                