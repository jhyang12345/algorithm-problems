# You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.
#
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

def non_decreasing_array(arr):
    smaller_than_before = 0
    if len(arr) < 2:
        return True
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            smaller_than_before += 1
    return smaller_than_before <= 1

if __name__ == '__main__':
    arr = [13, 4, 7]
    print(non_decreasing_array(arr))

    arr = [5, 1, 3, 2, 5]
    print(non_decreasing_array(arr))
