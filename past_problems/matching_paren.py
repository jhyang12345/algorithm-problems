text = "[(])"

def matches(text):
    q = []
    for ch in text:
        if ch in "[({":
            q.append(ch)
        elif ch == "]" and q[-1] == "[":
            q.pop()
        elif ch == ")" and q[-1] == "(":
            q.pop()
        elif ch == "}" and q[-1] == "{":
            q.pop()
    return len(q) == 0

print(matches(text))