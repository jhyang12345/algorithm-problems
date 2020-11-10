# N-Queens is the problem where you find a way to put
# n queens on a nxn chess board without them being able
# to attack each other. Given an integer n, return 1
# possible solution by returning all the queen's position.
#
# Here's an example and some starter code:
from pprint import pprint

pattern = [(3, 1), (-2, 1)]

def n_queens(n):
    board = [['.' for _ in range(n)] for __ in range(n)]
    start = (0, 0)
    spots = [start]
    for i in range(n - 1):
        x, y = pattern[i % 2]
        cur = spots[-1]
        spots.append((cur[0] + x, cur[1] + y))
    for spot in spots:
        x, y = spot
        board[x][y] = 'Q'

    for i in range(len(board)):
        board[i] = "".join(board[i])

    return "\n".join(board)


print(n_queens(5))
# There can be many answers
# [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]

# Q . . . .
# . . . Q .
# . Q . . .
# . . . . Q
# . . Q . .
