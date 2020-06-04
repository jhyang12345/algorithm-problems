arr = [-2, -3, 4, -1, -2, 1, -5, 10]

def kadanes(arr):
    cur_max = arr[0]
    max_till_now = cur_max
    for x in arr[1:]:
        max_till_now += x
        if max_till_now < 0:
            max_till_now = 0
        else:
            cur_max = max(cur_max, max_till_now)
    return cur_max

print(kadanes(arr))