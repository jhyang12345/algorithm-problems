# We have a list of tasks to perform, with a cooldown period. We can do multiple of these at the same time, but we cannot run the same task simultaneously.
#
# Given a list of tasks, find how long it will take to complete the tasks in the order they are input.
# tasks = [1, 1, 2, 1]
# cooldown = 2
# output: 7 (order is 1 _ _ 1 2 _ 1)
def findTime(arr, cooldown):
    tq = {}
    cap = 0
    for num in arr:
        if num not in tq:
            tq[num] = cap + num + cooldown
        else:
            cap = tq[num]
            tq[num] = cap + num + cooldown
    max_val = 0
    for num in tq:
        max_val = max(max_val, tq[num])
    return max_val - cooldown


print(findTime([1, 1, 2, 1], 2))
# 7
