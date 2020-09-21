# A chess board is an 8x8 grid. Given a knight at any position (x, y) and a number
# of moves k, we want to figure out after k random moves by a knight,
# the probability that the knight will still be on the chessboard.
# Once the knight leaves the board it cannot move again and will be considered off the board.
#
# Here's some starter code:

def knight_moves():
    a = [1, -1]
    b = [2, -2]
    moves = []
    for x in a:
        for y in b:
            moves.append([x, y])
    for y in a:
        for x in b:
            moves.append([x, y])
    return moves

def in_bounds(a, b):
    ret = True
    ret = ret and (0 <= a[0] + b[0] < 8)
    ret = ret and (0 <= a[1] + b[1] < 8)
    return ret

def is_knight_on_board(x, y, k):
    off = 0
    cache = [[0 for _ in range(8)] for __ in range(8)]
    cur = [[0 for _ in range(8)] for __ in range(8)]
    cache[x][y] = 1
    for i in range(k):
        for a in range(8):
            for b in range(8):
                moves = knight_moves()
                for move in moves:
                    if in_bounds([a, b], move):
                        cur[a + move[0]][b + move[1]] += cache[a][b]
                    else:
                        off += 1
        cache = cur
        cur = [[0 for _ in range(8)] for __ in range(8)]

    total = 0

    for i in range(8):
        for j in range(8):
            total += cache[i][j]
    print(total, off)
    return total / (total + off)


print(is_knight_on_board(0, 0, 1))
# 0.25
