def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    arr = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if right[j] < left[i]:
            arr.append(right[j])
            j += 1
        else:
            arr.append(left[i])
            i += 1
    while i < len(left):
        arr.append(left[i])
        i += 1
    while j < len(right):
        arr.append(right[j])
        j += 1
    return arr


print(merge_sort([1, 3, 2, 6, 4, 9, 8, 7]))
