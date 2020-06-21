# Given a mathematical expression with just single digits,
# plus signs, negative signs, and brackets, evaluate the expression.
# Assume the expression is properly formed.

# Possibly useful link
# https://leetcode.com/problems/basic-calculator/

def calculate(expression):
    # print(expression)
    words = expression.split()
    i = 0
    start = -1
    stack = []
    expressions = []
    magnitude = 1
    while i < len(words):
        cur = words[i]
        # print(stack)
        if cur == "(":
            stack.append(cur)
            if start == -1:
                start = i
        elif cur == ")":
            stack.pop()
            if len(stack) == 0:
                expressions.append(calculate(" ".join(words[start + 1:i])) * magnitude)
                start = -1
        elif start == -1:
            if cur == "-":
                magnitude = -1
            elif cur == "+":
                magnitude = 1
            else:
                if start == -1:
                    expressions.append(magnitude * int(cur))
        i += 1
    # print(expressions)
    return sum(expressions)


print(calculate('- ( 3 + ( 2 - 1 ) )'))
print(calculate('( 1 + ( 4 + 5 + 2 ) - 3 ) + ( 6 + 8 )'))
