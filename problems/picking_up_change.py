# Given a 2d n x m matrix where each cell has a certain amount
# of change on the floor, your goal is to start from the top left
# corner mat[0][0] and end in the bottom right corner mat[n - 1][m - 1]
# with the most amount of change. You can only move either left or down.
#
# Here's some starter code:

def max_change(mat):
    n = len(mat)
    m = len(mat[0])
    cache = [[0 for _ in range(m)] for __ in range(n)]
    cache[0][0] = mat[0][0]
    for y in range(n):
        for x in range(m):
            if y + 1 < n:
                cache[y + 1][x] = max(cache[y + 1][x], mat[y + 1][x] + cache[y][x])
            if x + 1 < m:
                cache[y][x + 1] = max(cache[y][x + 1], mat[y][x + 1] + cache[y][x])
    return cache[n - 1][m - 1]
mat = [
    [0, 3, 0, 2],
    [1, 2, 3, 3],
    [6, 0, 3, 2]
]

print(max_change(mat))
# 13
