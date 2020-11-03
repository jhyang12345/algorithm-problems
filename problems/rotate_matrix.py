# Given a square 2D matrix (n x n), rotate the matrix by 90 degrees clockwise.
#
# Here's an example and some starting code:

import math

dirs = [(0, 1), (1, 0), (0, -1) ,(-1, 0)]

def get_diff(x, y, mid):
    return max(abs(x * 10 - mid), abs(y * 10 - mid))

def get_dest_coord(mat, x, y):
    track = [(x, y)]
    n = len(mat)
    mid = (n - 1) * 5
    i = 0
    while True:
        x, y = track[-1]
        cur_diff = get_diff(x, y, mid)
        a, b = dirs[i]
        next = (x + a, y + b)
        next_x, next_y = next
        diff = get_diff(next_x, next_y, mid)
        if next == track[0]:
            break
        if diff != cur_diff:
            i += 1
            if i == 4:
                break
            continue
        else:
            track.append(next)
    return track

def rotate(mat):
    n = len(mat)
    for x in range(math.ceil(n / 2)):
        track = get_dest_coord(mat, x, x)
        moves = n - x - 1
        values = []
        for t in track:
            values.append(mat[t[0]][t[1]])
        new_values = values[- moves:] + values[: -moves]
        for i, t in enumerate(track):
            mat[t[0]][t[1]] = new_values[i]
    return mat



mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Looks like
# 1 2 3
# 4 5 6
# 7 8 9

# Looks like
# 7 4 1
# 8 5 2
# 9 6 3
print(rotate(mat))
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

mat = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10], [10, 11, 12, 13]]

print(rotate(mat))
