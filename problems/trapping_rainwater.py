# You have a landscape, in which puddles can form. 
# You are given an array of non-negative integers representing the elevation at each location.
# Return the amount of water that would accumulate if it rains.

def capacity(arr):
    left_to_right = [0 for _ in range(len(arr))]
    right_to_left = [0 for _ in range(len(arr))]
    cur_max = 0
    for i, x in enumerate(arr):
        cur_max = max(cur_max, x)
        left_to_right[i] = cur_max
    cur_max = 0
    for i in range(len(arr) - 1, -1, -1):
        x = arr[i]
        cur_max = max(cur_max, x)
        right_to_left[i] = cur_max
        left_to_right[i] = min(cur_max, left_to_right[i])
    ret = 0
    for i in range(len(arr)):
        ret += (left_to_right[i] - arr[i])
    return ret

print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
