# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.


def is_buddy_string(a, b):
    if len(a) != len(b):
        return False
    diffs = []
    dict = {}
    min_count = 1
    for i in range(len(a)):
        x = a[i]
        y = b[i]
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1
            min_count = max(min_count, dict[x])
        if x != y:
            diffs.append(i)
    if len(diffs) == 0:
        if min_count < 2:
            return False
        return True
    elif len(diffs) != 2:
        return False
    i = diffs[0]
    j = diffs[1]
    if a[i] == b[j] and a[j] == b[i]:
        return True
    return False


a = "ab"
b = "ba"
print(is_buddy_string(a, b))

a = "ab"
b = "ab"
print(is_buddy_string(a, b))

a = "aaaaaaabc"
b = "aaaaaaacb"
print(is_buddy_string(a, b))

a = "aa"
b = "aa"
print(is_buddy_string(a, b))
