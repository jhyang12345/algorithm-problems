# You are only allowed to perform 2 operations, multiply a number by 2,
# or subtract a number by 1. Given a number x and a number y,
# find the minimum number of operations needed to go from x to y.
#
# Here's an example and some starter code.

def min_operations(x, y):
    visited = {}
    visited[x] = True
    stack = [(x, 0)]
    while stack:
        cur, steps = stack.pop(0)
        visited[cur] = steps
        if cur == y:
            return steps
        mult_2 = cur * 2
        minus_1 = cur - 1
        if mult_2 not in visited:
            stack.append((mult_2, steps + 1))
        if minus_1 not in visited:
            stack.append((minus_1, steps + 1))
        



print(min_operations(6, 20))
# (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
# print 3
