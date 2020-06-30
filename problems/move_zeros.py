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
