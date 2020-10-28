# Given a list of sorted numbers (can be both negative or positive),
# return the list of numbers squared in sorted order.
#
# Here's an example and some starting code:

def square_numbers(nums):
    negs = []
    pos = []
    for num in nums:
        if num < 0:
            negs.append(num ** 2)
        else:
            pos.append(num ** 2)
    ret = []
    print(negs, pos)
    i = len(negs) - 1
    j = 0
    while i >= 0 or j < len(pos):
        if i >= 0 and j < len(pos):
            if negs[i] > pos[j]:
                ret.append(pos[j])
                j += 1
            else:
                ret.append(negs[i])
                i -= 1
        if i >= 0:
            ret.append(negs[i])
            i -= 1
        elif j < len(pos):
            ret.append(pos[j])
            j += 1
    return ret


print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
# [0, 1, 1, 9, 16, 25, 25]
