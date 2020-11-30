# Given a string, we want to remove 2 adjacent characters that are the same,
# and repeat the process with the new string until we can no longer perform the operation.
#
# Here's an example and some starter code:

def remove_adjacent_dup(s):
    stack = []
    for ch in s:
        if not stack or ch != stack[-1]:
            stack.append(ch)
        else:
            stack.pop()
    return stack

print(remove_adjacent_dup("cabba"))
# Start with cabba
# After remove bb: caa
# After remove aa: c
# print c
