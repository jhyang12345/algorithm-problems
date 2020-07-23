# Given a list of words, and an arbitrary alphabetical order, verify that the words are in order of the alphabetical order.

def is_sorted(arr, order):
    dict = {x:i for i, x in enumerate(list(order))}
    for i in range(1, len(arr)):
        x = 0
        a = arr[i - 1]
        b = arr[i]
        while x < len(a) and x < len(b):
            char_a = a[x]
            char_b = b[x]
            if dict[char_a] > dict[char_b]:
                return False
            else:
                x += 1
        if len(a) > len(b):
            return False
    return True



print(is_sorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
print(is_sorted(["zyx", "zyxw", "zyxwy"],
               "zyxwvutsrqponmlkjihgfedcba"))
