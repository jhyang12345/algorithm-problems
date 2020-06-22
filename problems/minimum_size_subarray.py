def min_sub_array(arr, s):
    start = 0
    end = 1
    cur_sum = sum(arr[start:end])
    min_length = len(arr) + 1
    while True:
        if cur_sum >= s:
            min_length = min(min_length, end - start)
            cur_sum -= arr[start]
            start += 1
            if end <= start:
                cur_sum += arr[end]
                end += 1
        else:
            if end == len(arr):
                break
            cur_sum += arr[end]
            end += 1
            if end > len(arr):
                break
    if min_length == len(arr) + 1:
        return 0
    return min_length

print(min_sub_array([2, 3, 1, 2, 4, 3], 7))
print(min_sub_array([2, 3, 1, 2, 4, 3], 10))
