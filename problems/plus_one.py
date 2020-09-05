# Given a non-empty array where each element represents a digit of a non-negative integer,
# add one to the integer. The most significant digit is at the front of the array and
# each element in the array contains only one digit. Furthermore, the integer does not
# have leading zeros, except in the case of the number '0'.
#
# Example:
# Input: [2,3,4]
# Output: [2,3,5]
def plusOne(digits):
    n = len(digits)
    val = 1
    for i in range(n - 1, -1, -1):
        cur = digits[i]
        cur += val
        if cur < 10:
            val = 0
        digits[i] = (cur % 10)
    return digits



num = [2, 9, 9]
print(plusOne(num))
# [3, 0, 0]
