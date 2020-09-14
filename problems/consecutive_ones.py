# Return the longest run of 1s for a given integer n's binary representation.
#
# Example:
# Input: 242
# Output: 4
# 242 in binary is 0b11110010, so the longest run of 1 is 4.

def longest_run(n):
    char = ""
    last = "0"
    count = 0
    ret = 0
    while n:
        r = n % 2
        if r == 0:
            char += "0"
            last = "0"
            count = 0
        elif r == 1:
            char += "1"
            last = "1"
            if last == "1":
                count += 1
        ret = max(ret, count)
        n = n // 2
    return ret


print(longest_run(242))
# 4
