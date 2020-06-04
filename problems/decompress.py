text = "2[3[a]b]"

def decompress(text):
    ret = ""
    expressionStarted = False
    start = -1
    end = -1
    num = ""
    stack = []
    for i, ch in enumerate(text):
        # print(stack)
        if ch.isnumeric():
            if not expressionStarted:
                expressionStarted = True
            if start == -1:
                num += ch
        elif ch == "[":
            if start == -1:
                start = i
            stack.append(ch)
        elif ch == "]":
            stack.pop()
            if len(stack) == 0:
                end = i
                print(num)
                ret += int(num) * decompress(text[start + 1:end])
                expressionStarted = False
                start = -1
                end = -1
                num = ""
        elif start == -1 and ch.isalpha():
            ret += ch
    return ret

print(decompress(text))

# abcabcabcababababc
# abcabcabcababababc