# Given a string, determine if there is a way to arrange the string
# such that the string is a palindrome. If such arrangement exists,
# return a palindrome (There could be many arrangements). Otherwise return None.
#
# Here's some starter code:
import math

def is_palindrome(s):
    left_end = math.ceil(len(s) / 2)
    right_start = len(s) // 2
    return s[:left_end] == s[right_start:][::-1]

def find_palindrome(s):
    for i in range(len(s)):
        flag = is_palindrome(s[i:] + s[:i])
        if flag:
            return s[i:] + s[:i]

print(find_palindrome('momom'))
# momom
print(find_palindrome('omomm'))
