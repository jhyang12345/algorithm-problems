# You are given an array of integers. Return all the permutations of this array.

def permute(nums):
    ret = []
    if len(nums) == 1:
        return [nums]
    for i in range(len(nums)):
        x = nums[i]
        ps = permute(nums[i + 1:] + nums[:i])
        for arr in ps:
            ret.append([x] + arr)
    return ret

print(permute([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
