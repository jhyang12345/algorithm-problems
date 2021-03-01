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

# https://leetcode.com/problems/jump-game/submissions/
def jump_game_2(arr):
    n = len(arr)
    cur_max = 0
    for i, x in enumerate(arr):
        if cur_max < i:
            return False
        cur_max = max(i + x, cur_max)
        if n - 1 <= cur_max:
            return True



nums = [2,3,1,1,4]
print(jump_game_2(nums))

nums = [0, 2, 3]
print(jump_game_2(nums))

nums = [3,0,8,2,0,0,1]
print(jump_game_2(nums))
