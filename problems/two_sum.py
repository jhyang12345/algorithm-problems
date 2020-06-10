
def two_sum(arr, x):
    dict = {}
    for num in arr:
        if num in dict:
            return True
        dict[x - num] = 0
    return False

if __name__ == '__main__':
    arr = [4, 7, 1, -3, 2]
    x = 5
    print(two_sum(arr, x))
    arr = [4, 7, 1, -3, 2]
    x = 2
    print(two_sum(arr, x))
