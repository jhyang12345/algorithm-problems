def triangle_sum(arr):
    cur = arr[0]
    for line in arr[1:]:
        n = len(line)
        for i in range(n):
            if i == 0:
                line[i] = line[i] + cur[i]
            elif i == n - 1:
                line[i] = line[i] + cur[i - 1]
            else:
                line[i] = min(cur[i], cur[i - 1]) + line[i]
        cur = line
    return min(cur)

# https://leetcode.com/problems/triangle/submissions/

print(triangle_sum([[2],[3,4],[6,5,7],[4,1,8,3]]))
