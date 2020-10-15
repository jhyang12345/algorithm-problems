# A maze is a matrix where each cell can either be a 0 or 1.
# A 0 represents that the cell is empty, and a 1 represents
# a wall that cannot be walked through. You can also only travel either right or down.
#
# Given a nxm matrix, find the number of ways someone can go
# from the top left corner to the bottom right corner.
# You can assume the two corners will always be 0.
#
# Example:
# Input: [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
# # 0 1 0
# # 0 0 1
# # 0 0 0
# Output: 2
# The two paths that can only be taken in the above example are:
# down -> right -> down -> right, and down -> down -> right -> right.
#
# Here's some starter code:

def paths_through_maze(maze):
    n = len(maze)
    m = len(maze[0])
    cache = [[0 for _ in range(m)] for __ in range(n)]
    cache[0][0] = 1
    for x in range(n):
        for y in range(m):
            if y < m - 1 and maze[x][y + 1] != 1:
                cache[x][y + 1] += cache[x][y]
            if x < n - 1 and maze[x + 1][y] != 1:
                cache[x + 1][y] += cache[x][y]
    return cache[n - 1][m - 1]

print(paths_through_maze([[0, 1, 0],
                          [0, 0, 1],
                          [0, 0, 0]]))
# 2
