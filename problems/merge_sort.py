import random

def merge(a, b):
    ret = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        x = a[i]
        y = b[j]
        if x < y:
            ret.append(x)
            i += 1
        else:
            ret.append(y)
            j += 1
    while i < len(a):
        x = a[i]
        ret.append(x)
        i += 1
    while j < len(b):
        y = b[j]
        ret.append(y)
        j += 1
    return ret

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    n = len(arr)
    mid = n // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

arr = list(range(1, 21))
random.shuffle(arr)
print(arr)
print(merge_sort(arr))