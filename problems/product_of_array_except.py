# You are given an array of integers. Return an array of the same size where the element at each
# index is the product of all the elements in the original array except for the element at that index.
#
# For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].

def product_of_array(arr):
    n = len(arr)
    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]
    for i in range(n):
        if i == 0:
            left[i] = arr[i]
        else:
            left[i] = (arr[i] * left[i - 1])
    for i in range(n - 1, -1, -1):

        if i == n - 1:
            right[i] = arr[i]
        else:
            right[i] = (arr[i] * right[i + 1])
    ret = []
    for i in range(n):
        l = 1
        r = 1
        if i > 0:
            l = left[i - 1]
        if i < n - 1:
            r = right[i + 1]
        ret.append(r * l)
    return ret

arr = [1, 2, 3, 4, 5]
print(product_of_array(arr))
