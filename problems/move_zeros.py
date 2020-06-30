def move_zeros(arr):
    stack = []
    for x in arr:
        if x != 0:
            stack.append(x)
    stack += ((len(arr) - len(stack))) * [0]
    return stack

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
print(nums)
print(move_zeros(nums))


def move_zeros_2(arr):
    last_num = 0
    for i in range(len(arr)):
        cur = arr[i]
        if cur != 0:
            if last_num != i:
                arr[last_num] = cur
                arr[i] = 0
            last_num += 1
    return arr



nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
print(nums)
print(move_zeros_2(nums))

nums = [1, 2, 3, 4, 0]
print(nums)
print(move_zeros_2(nums))
