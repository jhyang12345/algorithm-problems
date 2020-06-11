# Given a list of numbers, where every number shows up twice except for one number, find that one number.
# Try to solve with only O(1) space
# look into https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

def find_non_duplicate(arr):
    arr.sort()
    for i in range(len(arr)):
        if i > 0 and (i < len(arr) - 1):
            if arr[i] == arr[i-1]:
                continue
            elif arr[i] == arr[i + 1]:
                continue
            return arr[i]
        elif i > 0:
            if arr[i] != arr[i - 1]:
                return arr[i]
        elif i < len(arr) - 1:
            if arr[i] != arr[i + 1]:
                return arr[i]

if __name__ == '__main__':
    arr = [4, 3, 2, 4, 1, 3, 2]
    print(find_non_duplicate(arr))
