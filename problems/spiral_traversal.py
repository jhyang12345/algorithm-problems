def next_valid(x, y, dir, visited):
    a = x + dir[0]
    b = y + dir[1]
    if a >= len(visited) or a < 0:
        return False
    elif b >= len(visited[0]) or b < 0:
        return False
    elif visited[a][b]:
        return False
    return True

def matrix_spiral(grid):
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x = 0
    y = 0
    i = 0
    cur_dir = directions[i]
    visited = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]
    while True:
        visited[x][y] = True
        print(grid[x][y])
        if next_valid(x, y, cur_dir, visited):
            x += cur_dir[0]
            y += cur_dir[1]
        else:
            i = (i + 1) % 4
            cur_dir = directions[i]
            if next_valid(x, y, cur_dir, visited):
                x += cur_dir[0]
                y += cur_dir[1]
            else:
                break

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]
matrix_spiral(grid)
