import sys

def is_valid_parentheses(text):
    stack = []
    print(text)
    for x in text:
        if len(stack):
            last = stack[-1]
        else:
            last = ''
        if x == ")" and last == "(":
            stack.pop()
        elif x == "]" and last == "[":
            stack.pop()
        elif x == "}" and last == "{":
            stack.pop()
        else:
            stack.append(x)
    return len(stack) == 0

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    for _ in range(n):
        text = sys.stdin.readline().strip()
        is_valid = is_valid_parentheses(text)
        print(is_valid)
