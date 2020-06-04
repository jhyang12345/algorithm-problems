arr = [-2, -3, 4, -1, -2, 1, -5, 10]

def kadanes(arr):
    cur_max = arr[0]
    max_til_now = cur_max
    for x in arr[1:]:
        if cur_max < 0:
            cur_max = x
        else:
            cur_max += x
        max_til_now = max(max_til_now, cur_max)
    return max_til_now

print(kadanes(arr))