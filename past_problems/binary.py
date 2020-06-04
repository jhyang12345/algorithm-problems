def binary(arr, num):
    lo = 0
    hi = len(arr) + 1
    mid = (lo + hi) // 2
    while lo + 1 < hi:
        cur = arr[mid]
        if cur <= num:
            lo = mid
        else:
            hi = mid
        mid = (lo + hi) // 2
    print(mid, arr[mid])


arr = list(range(1, 21))
num = 5

binary(arr, num)