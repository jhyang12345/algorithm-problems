# MS Excel column titles have the following pattern: A, B, C, ..., Z, AA, AB, ..., AZ, BA, BB, ..., ZZ, AAA, AAB, ... etc.
# In other words, column 1 is named "A", column 2 is "B", column 26 is "Z", column 27 is "AA" and so forth.
# Given a positive integer, find its corresponding column name.
# Examples:
# Input: 26
# Output: Z
#
# Input: 51
# Output: AY
#
# Input: 52
# Output: AZ
#
# Input: 676
# Output: YZ
#
# Input: 702
# Output: ZZ
#
# Input: 704
# Output: AAB
def convertToTitle(n):
    s = ""
    for i in range(65,91):
        s = s + chr(i)
    st = ""
    while n:
        n = n - 1
        st = s[n % 26] + st
        n = n // 26
    return st

input1 = 1
input2 = 456976
input3 = 28
print(convertToTitle(input1))
# A
print(convertToTitle(input2))
# YYYZ
print(convertToTitle(input3))

print(convertToTitle(52))
