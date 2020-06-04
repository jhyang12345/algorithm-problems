arr = [10, 30, 40, 50, 20]

def min_kth_jump(arr, k):
    n = len(arr)
    cache = [-1 for _ in range(n)]
    cache[0] = 0
    for i in range(n):
        cur = arr[i]
        for j in range(1, k + 1):
            if i + j < n:
                next = arr[i + j]
                if cache[i + j] == -1:
                    cache[i + j] = cache[i] + abs(next - cur)
                cache[i + j] = min(cache[i + j], cache[i] + abs(next - cur))
    return cache[-1]

def min_kth_jump_2(arr, k):
    n = len(arr)
    cache = [-1 for _ in range(n)]
    cache[0] = 0
    for i in range(n):
        cur = arr[i]
        for j in range(1, k + 1):
            if i + j < n:
                next = arr[i + j]
                if cache[i + j] == -1:
                    cache[i + j] = cache[i] + abs(cur - next)
                cache[i + j] = min(cache[i + j], cache[i] + abs(cur - next))
    return cache[-1]

def min_kth_jump_3(arr, k):
    n = len(arr)
    cache = [-1 for _ in range(n)]
    cache[0] = 0
    for i in range(n):
        next = arr[i]
        for j in range(1, k + 1):
            if i - j >= 0:
                cur = arr[i - j]
                if cache[i] == -1:
                    cache[i] = cache[i - j] + abs(cur - next)
                cache[i] = min(cache[i], cache[i - j] + abs(cur - next))
    return cache[-1]

print(min_kth_jump(arr, 3))
print(min_kth_jump_2(arr, 3))
print(min_kth_jump_3(arr, 3))