# You are given two strings, A and B. Return whether A can be shifted some number of times to get B.
#
# Eg. A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get B.
# A = abc and B= acb should return false.

# should maybe look into using string search algorithm?.?

def is_shifted(a, b):
    return a in b * 2

print(is_shifted('abcde', 'cdeab'))
