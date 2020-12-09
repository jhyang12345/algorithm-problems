# Reshaping a matrix means to take the same elements in a matrix but change the row and column length.
# This means that the new matrix needs to have the same elements filled in the same row order as the old matrix.
# Given a matrix, a new row size x and a new column size y, reshape the matrix. If it is not possible to reshape, return None.
#
# Here's an example and some starter code.

def reshape_matrix(mat, x, y):
    n = len(mat)
    m = len(mat[0])
    if n * m != x * y:
        return None
    stack = []
    cache = [[0 for _ in range(x)] for __ in range(y)]
    for i in range(n):
        for j in range(m):
            stack.append(mat[i][j])
    index = 0
    for i in range(y):
        for j in range(x):
            cache[i][j] = stack[index]
            index += 1
    return cache



print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
# [[1], [2], [3], [4]]

print(reshape_matrix([[1, 2], [3, 4]], 2, 3))
# None
