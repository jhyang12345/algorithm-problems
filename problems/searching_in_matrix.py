# Given a matrix that is organized such that the numbers will always
# be sorted left to right, and the first number of each row will always
# be greater than the last element of the last row (mat[i][0] > mat[i - 1][-1]),
# search for a specific value in the matrix and return whether it exists.
#
# Here's an example and some starter code.

def searchMatrix(mat, value):
    n = len(mat)
    m = len(mat[0])
    total = n * m
    lo = 0
    hi = total
    mid = (lo + hi) // 2
    while lo + 1 < hi:
        x = mid // m
        y = mid % m
        print(x, y)
        cur = mat[x][y]
        if cur < value:
            lo = mid
        elif cur > value:
            hi = mid
        else:
            return True
        mid = (lo + hi) // 2
    return False

mat = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31],
]

print(searchMatrix(mat, 4))
# False

print(searchMatrix(mat, 10))
# True
