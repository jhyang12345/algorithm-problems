text = "3[abc]4[ab]c"
numbers = "1234567890"
alphas = "abcdefghijklmnopqrstuvwxyz"

def decompress(text):
    ret = ""
    num = ""
    start = -1
    end = -1
    q = []
    for i, ch in enumerate(text):
        if ch in numbers:
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
                ret += int(num) * decompress(text[start:end])
                start = -1
                end = -1
                num = ""
        elif start == -1:
            ret += ch
    return ret

print(decompress(text))