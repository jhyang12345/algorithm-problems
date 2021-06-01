# Problem
# Charles defines the goodness score of a string as the number of indices i
# such that Si≠SN−i+1 where 1≤i≤N/2 (1-indexed). For example, the string
# CABABC has a goodness score of 2 since S2≠S5 and S3≠S4.
#
# Charles gave Ada a string S of length N, consisting of uppercase letters
# and asked her to convert it into a string with a goodness score of K.
# In one operation, Ada can change any character in the string to any uppercase letter.
# Could you help Ada find the minimum number of operations required to transform
# the given string into a string with goodness score equal to K?


import sys


t = int(sys.stdin.readline())

def cal_goodness_diff(text, k):
    n = len(text) - 1
    left = 0
    right = n
    ret = 0
    while left < right:
        if text[left] != text[right]:
            ret += 1
        left += 1
        right -= 1
    return abs(ret - k)


for i in range(t):
    n, k = list(map(int, sys.stdin.readline().split()))
    text = sys.stdin.readline().strip()
    ret = cal_goodness_diff(text, k)
    print(f"Case #{i + 1}: {ret}")
