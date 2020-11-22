# Given a list of numbers, for each element find the next element that is larger than the current element.
# Return the answer as a list of indices. If there are no elements larger than the current element, then use -1 instead.
#
# Here's an example and some starter code:

def larger_next_number(nums):
    stack = []
    ret = [-1] * len(nums)
    for i in range(len(nums)):
        x = nums[i]
        while stack:
            index = stack[-1]
            if x > nums[index]:
                stack.pop()
                ret[index] = i
            else:
                break
        stack.append(i)
    return ret

# print [2, 2, 3, 4, -1, -1]
print(larger_next_number([3, 2, 5, 6, 9, 8]))


print(larger_next_number([1, 6, 4, 6, 9, 8]))
