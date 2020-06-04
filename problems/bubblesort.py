import random

def bubblesort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 2, i - 1, -1):
            a = arr[j]
            b = arr[j + 1]
            if a > b:
                arr[j] = b
                arr[j + 1] = a
    print(arr)

arr = list(range(1, 21))
random.shuffle(arr)
print(arr)

bubblesort(arr)