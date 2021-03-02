def max_overlapping_intervals(pairs):
    steps = []
    for pair in pairs:
        steps.append([pair[0], 1])
        steps.append([pair[1], -1])
    steps.sort()
    i = 0
    count = 0
    ret = 0
    index = 0
    while i < len(steps):
        val = steps[i][0]
        count += steps[i][1]
        i += 1
        ret = max(count, ret)
        if ret == count:
            index = val
    ret = max(count, ret)
    if ret == count:
        index = val
    return ret

# https://www.geeksforgeeks.org/find-the-point-where-maximum-intervals-overlap/



pairs = [[1, 8], [2, 5], [5, 6], [3, 7]]
print(max_overlapping_intervals(pairs))
