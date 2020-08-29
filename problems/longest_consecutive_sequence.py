def longest_consecutive(nums):
    nums.sort()
    prev = nums[0]
    count = 1
    ret = 1
    for x in nums[1:]:
        if x == prev + 1:
            count += 1
            prev = x
        else:
            count = 1
            prev = x
        ret = max(ret, count)
    return ret

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# 4
