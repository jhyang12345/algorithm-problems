# Given two strings, find if there is a one-to-one mapping of characters between the two strings.
#
# Example
# Input: abc, def
# Output: True # a -> d, b -> e, c -> f
#
# Input: aab, def
# Ouput: False # a can't map to d and e
# Here's some starter code:

def has_character_map(str1, str2):
    a = set(list(str1))
    b = set(list(str2))
    return len(a) == len(b)

print(has_character_map('abc', 'def'))
# True
print(has_character_map('aac', 'def'))
# False

# Solve later
# https://leetcode.com/problems/isomorphic-strings/
