# Given an unsorted integer array, find the smallest missing positive integer.

def first_missing_positive(arr):
    upper_bound = len(arr) + 1
    is_present = [0] * (upper_bound + 1)
    for x in arr:
        if x <= 0:
            upper_bound -= 1
        elif x > upper_bound:
            upper_bound -= 1
        else:
            is_present[x] = 1
    for x in range(1, upper_bound + 1):
        if is_present[x] == 0:
            return x
    return 1


print(first_missing_positive([1, 2, 0]))
print(first_missing_positive([3,4,-1,1]))
print(first_missing_positive([7, 8, 9, 11, 12]))
