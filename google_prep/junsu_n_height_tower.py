# there are 4 types of blocks with height 1, 2, 3, 4 find the number of ways to build a tower of height # NOTE:

def get_tower_count(n):
    heights = [1, 2, 3, 4]
    cache = [0] * (n + 1)
    cache[0] = 1
    for i in range(n):
        for j in heights:
            if i + j <= n:
                cache[i + j] = cache[i + j] + cache[i]
    return cache[n]

print(get_tower_count(5))
print(get_tower_count(4))
print(get_tower_count(2))
