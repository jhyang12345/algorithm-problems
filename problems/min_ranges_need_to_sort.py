def findRange(nums):
    s = sorted(nums)
    start = len(s)
    end = 0
    for i in range(len(s)):
        if s[i] != nums[i]:
            start = min(i, start)
            end = max(i, start)
    return (start, end)

print(findRange([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)
