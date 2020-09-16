# Given an integer, check if that integer is a palindrome. For this problem do not
# convert the integer to a string to check if it is a palindrome.

import math

def is_palindrome(n):
    print(n)
    i = 0
    while (10 ** i) <= n:
        i += 1
    i -= 1
    cap = i
    i = 0
    while i <= cap // 2:
        left = round(n / (10 ** (i + 1)) % 1 * 10) // 1
        right = round(n / (10 ** (cap - i + 1)) % 1 * 10) // 1
        if left != right:
            return False
        i += 1
    return True



print(is_palindrome(1234321))
# True
print(is_palindrome(1234322))
# False
print(is_palindrome(121))
# False
