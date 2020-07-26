# You are given a string of parenthesis. Return the minimum number of parenthesis that would need to be
#  removed in order to make the string valid. "Valid" means that each open parenthesis has a
#  matching closed parenthesis.

# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

def count_invalid_parenthesis(string):
    stack = []
    ret = 0
    for x in string:
        if x == "(":
            stack.append("(")
        elif x == ")":
            if stack:
                stack.pop()
            else:
                ret += 1
    ret += len(stack)
    return ret

print(count_invalid_parenthesis("()())()"))
print(count_invalid_parenthesis(")("))
print(count_invalid_parenthesis("()"))
