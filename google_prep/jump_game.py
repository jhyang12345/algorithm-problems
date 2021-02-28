def jump_game(arr):
    n = len(arr)
    cache = [False] * n
    cache[0] = True
    for i in range(n):
        steps = arr[i]
        for j in range(i, min(i + steps + 1, n)):
            cache[j] = cache[j] | cache[i]
            if j == n -1 and cache[j]:
                return True
    return cache[n - 1]


nums = [2,3,1,1,4]
print(jump_game(nums))

nums = [0, 2, 3]
print(jump_game(nums))
