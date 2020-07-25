# Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks),
# count the number of islands present in the grid. The definition of an island is as follows:
# 1.) Must be surrounded by water blocks.
# 2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
# Assume all edges outside of the grid are water.

def get_next_blocks(cur, grid):
    x, y = cur
    ret = []
    n = len(grid)
    m = len(grid[0])
    if x > 0:
        a = x - 1
        b = y
        if grid[a][b] == 1:
            ret.append([a, b])
    if x < n - 1:
        a = x + 1
        b = y
        if grid[a][b] == 1:
            ret.append([a, b])
    if y > 0:
        a = x
        b = y - 1
        if grid[a][b] == 1:
            ret.append([a, b])
    if y < m - 1:
        a = x
        b = y + 1
        if grid[a][b] == 1:
            ret.append([a, b])
    return ret



def num_islands(grid):
    n = len(grid)
    m = len(grid[0])
    islands = 0
    for i in range(n):
        for j in range(m):
            cur = grid[i][j]
            if cur == 0:
                continue
            else:
                islands += 1
                queue = [[i, j]]
                while queue:
                    x, y = queue.pop(0)
                    grid[x][y] = 0
                    next_blocks = get_next_blocks([x, y], grid)
                    queue += next_blocks
    return islands

grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]

print(num_islands(grid))


grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0]]

print(num_islands(grid))
