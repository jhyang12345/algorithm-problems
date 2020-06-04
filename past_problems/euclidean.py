def euclidean(a, b):
    if b == 0:
        return a
    if a > b:
        return euclidean(b, a % b)
    else:
        return euclidean(a, b % a)

print(euclidean(54, 24))