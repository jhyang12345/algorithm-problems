# Kaprekar's Constant is the number 6174. This number is special because it
# has the property where for any 4-digit number that has 2 or more unique digits,
# if you repeatedly apply a certain function it always reaches the number 6174.
#
# This certain function is as follows:
# - Order the number in ascending form and descending form to create 2 numbers.
# - Pad the descending number with zeros until it is 4 digits in length.
# - Subtract the ascending number from the descending number.
# - Repeat.
#
# Given a number n, find the number of times the function needs
# to be applied to reach Kaprekar's constant. Here's some starter code:
#
# KAPREKAR_CONSTANT = 6174

def num_kaprekar_iterations(n):
    a = 0
    b = 0
    nums = list(str(n))
    while len(nums) < 4:
        nums.append('0')
    count = 0
    while True:
        l = sorted(nums)
        a = int("".join(l)[::-1])
        b = int("".join(l))
        nums = list(str(a - b))
        count += 1
        if nums == ['6', '1', '7', '4']:
            return count

print(num_kaprekar_iterations(123))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)
