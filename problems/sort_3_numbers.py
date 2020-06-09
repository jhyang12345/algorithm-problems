import sys

# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
#
# Example 1:
# Input: [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]

def sort_via_dict(arr):
    numbers = [1, 2, 3]
    dict = {1:0, 2:0, 3:0}
    for x in arr:
        dict[x] += 1
    ret = []
    for x in dict:
        ret = ret + [x] * dict[x]
    return ret

def sort_via_constant(arr):
    numbers = [1, 2, 3]
    last_index = 0
    for x in numbers:
        for i in range(len(arr)):
            cur = arr[i]
            if cur == x and last_index <= i:
                arr[i] = arr[last_index]
                arr[last_index] = x
                last_index += 1
    return arr


if __name__ == '__main__':
    arr = [3, 3, 2, 1, 3, 2, 1]
    print(sort_via_dict(arr))
    arr = [3, 3, 2, 1, 3, 2, 1, 2]
    print(sort_via_constant(arr))
    arr = [3, 3, 1, 1, 2, 2]
    print(sort_via_constant(arr))
