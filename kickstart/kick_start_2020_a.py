# Input
# The first line of the input gives the number of test cases, T.
#  T test cases follow. Each test case begins with a single line
#  containing the two integers N and B. The second line contains N integers.
#  The i-th integer is Ai, the cost of the i-th house.
#
# Output
# For each test case, output one line containing Case #x: y,
# where x is the test case number (starting from 1) and y is the maximum number of houses you can buy.
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56

import sys

def get_max_houses(b, costs):
    costs.sort()
    count = 0
    budget = b
    for x in costs:
        if x <= budget:
            budget -= x
            count += 1
    return count


if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for i in range(t):
        n, b = list(map(int, sys.stdin.readline().split()))
        costs = list(map(int, sys.stdin.readline().split()))
        print(f"Case #{i + 1}: {get_max_houses(b, costs)}")
