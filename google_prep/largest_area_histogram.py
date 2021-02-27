def largest_rectangle_area(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    mid = n // 2
    ret = 0
    ret = max(ret, largest_rectangle_area(arr[:mid]))
    ret = max(ret, largest_rectangle_area(arr[mid:]))
    left = mid - 1
    right = mid
    height = min(arr[left], arr[right])
    while left >= 0 and right < n:
        if left == 0 and right == n - 1:
            break
        if left == 0:
            right += 1
            height = min(height, arr[right])
        elif right == n - 1:
            left -= 1
            height = min(height, arr[left])
        elif arr[left - 1] < arr[right + 1]:
            right += 1
            height = min(height, arr[right])
        else:
            left -= 1
            height = min(height, arr[left])
        ret = max(ret, (right - left + 1) * height)
    return ret

print(largest_rectangle_area([2,1,5,6,2,3]))
