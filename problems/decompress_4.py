text = "3[abc]4[ab]c"
numbers = "1234567890"
alphas = "abcdefghijklmnopqrstuvwxyz"

def decompress(text):
    start = -1
    num = ""
    ret = ""
    q = []
    for i, ch in enumerate(text):
        if ch in numbers and start == -1:
            num += ch
        elif ch == "[":
            if start == -1:
                start = i + 1
            q.append(ch)
        elif ch == "]":
            q.pop()
            if len(q) == 0:
                ret += int(num) * decompress(text[start:i])
                start = -1
                num = ""
        elif ch in alphas and start == -1:
            ret += ch
    return ret
        
print(decompress(text))