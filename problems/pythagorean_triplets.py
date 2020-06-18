# Given a list of numbers, find if there exists a pythagorean triplet in that list.
# A pythagorean triplet is 3 variables a, b, c where a2 + b2 = c2

def has_pythagorean_triplet(arr):
    squares = [x ** 2 for x in sorted(arr)]
    dict = {}
    for x in squares:
        dict[x] = 1
    for i in range(len(squares) - 2):
        for j in range(i + 1, len(squares) - 1):
            if (squares[i] + squares[j]) in dict:
                return True
    else:
        return False


arr = [3, 5, 12, 5, 13]
print(has_pythagorean_triplet(arr))

arr = [3, 3, 3]
print(has_pythagorean_triplet(arr))
