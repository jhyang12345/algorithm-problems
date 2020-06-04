

def comb(a, b):
    if a == b or b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return (comb(a - 1, b) + comb(a - 1, b - 1))

print(comb(7, 3))