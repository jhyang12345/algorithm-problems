# Given a list of numbers, find the smallest window to sort such that the whole list will be sorted.
# If the list is already sorted return (0, 0). You can assume there will be no duplicate numbers.
#
# Example:
# Input: [2, 4, 7, 5, 6, 8, 9]
# Output: (2, 4)
# Explanation: Sorting the window (2, 4) which is [7, 5, 6] will also means that the whole list is sorted.

def min_window_to_sort(nums):
    s_list = sorted(nums)
    start = -1
    end = -1
    for i, x in enumerate(nums):
        if x != s_list[i]:
            if start == -1:
                start = i
            end = i
    if start == -1:
        return [0, 0]
    return [start, end]

print(min_window_to_sort([2, 4, 7, 5, 6, 8, 9]))
# (2, 4)
