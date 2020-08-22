# Given a number of integers, combine them so it would create the largest number.

def largest_num(nums):
    arr = list(map(str, nums))
    arr.sort()

    ret = ""
    for x in arr[::-1]:
        ret += x
    return int(ret)

nums = [17, 7, 2, 45, 72]
print(largest_num(nums))
