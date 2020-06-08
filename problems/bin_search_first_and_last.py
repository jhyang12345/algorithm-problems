import os
import sys

def find_lower(arr, value):
    print(arr, value)
    lo = 0
    hi = len(arr)
    mid = (lo + hi) // 2
    while lo + 1 < hi:
        cur = arr[mid]
        if cur < value:
            lo = mid
        else:
            hi = mid
        mid = (lo + hi) // 2
    return mid + 1, arr[mid + 1]

def find_upper(arr, value):
    lo = 0
    hi = len(arr)
    mid = (lo + hi) // 2
    while lo + 1 < hi:
        cur = arr[mid]
        if cur > value:
            hi = mid
        else:
            lo = mid
        mid = (lo + hi) // 2
    return mid, arr[mid]

if __name__ == '__main__':
    arr = [1,3,3,5,7,8,9,9,9,15]
    value = 9
    print(find_lower(arr, value))
    print(find_upper(arr, value))

    arr = [100, 150, 150, 153]
    value = 150
    print(find_lower(arr, value))
    print(find_upper(arr, value))

    arr = [1,2,3,4,5,6,10]
    value = 9
    print(find_lower(arr, value))
    print(find_upper(arr, value))

    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    value = 2
    print(find_lower(arr, value))
    print(find_upper(arr, value))
