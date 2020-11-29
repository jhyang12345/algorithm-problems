# Given a positive integer n, find all primes less than n.
#
# Here's an example and some starter code:

def find_primes(n):
    arr = [True] * (n)
    arr[0] = False
    arr[1] = False
    for x in range(2, n):
        if arr[x] == True:
            for y in range(x, n, x):
                if x == y:
                    continue
                else:
                    arr[y] = False
    ret = []
    for i in range(len(arr)):
        if arr[i]:
            ret.append(i)
    return ret


print(find_primes(14))
# [2, 3, 5, 7, 11, 13]
