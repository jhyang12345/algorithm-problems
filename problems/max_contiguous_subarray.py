def max_subarray_sum(arr):
    cur_max = arr[0]
    max_til_now = arr[0]
    for x in arr[1:]:
        cur_max = max(x, cur_max + x)
        max_til_now = max(max_til_now, cur_max)
    return max_til_now

print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
