# Given a string with only ( and ), find the minimum number of characters to add
# or subtract to fix the string such that the brackets are balanced.
#
# Example:
# Input: '(()()'
# Output: 1
# Explanation:
#
# The fixed string could either be ()() by deleting the first bracket,
# or (()()) by adding a bracket. These are not the only ways of fixing the string,
# there are many other ways by adding it in different positions!

def fix_brackets(s):
    stack = []
    for x in s:
        if x == '(':
            stack.append('(')
        elif x == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
    return len(stack)

print(fix_brackets('(()()'))
