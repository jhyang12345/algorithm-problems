def transpose(mat):
    n = len(mat)
    m = len(mat[0])
    cache = [[0 for _ in range(n)] for __ in range(m)]
    for x in range(n):
        for y in range(m):
            cache[y][x] = mat[x][y]
    return cache

mat = [
    [1, 2, 3],
    [4, 5, 6],
]

print(transpose(mat))
# [[1, 4],
#  [2, 5],
#  [3, 6]]
