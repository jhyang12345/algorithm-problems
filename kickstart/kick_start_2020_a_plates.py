# Dr. Patel has N stacks of plates. Each stack contains K plates.
# Each plate has a positive beauty value, describing how beautiful it looks.
#
# Dr. Patel would like to take exactly P plates to use for dinner tonight.
# If he would like to take a plate in a stack, he must also take all of the plates above it in that stack as well.
#
# Help Dr. Patel pick the P plates that would maximize the total sum of beauty values.
#
# Input
# The first line of the input gives the number of test cases, T. T test cases follow.
# Each test case begins with a line containing the three integers N, K and P. Then, N lines follow.
# The i-th line contains K integers, describing the beauty values of each stack of plates from top to bottom.
import sys

def get_max_beauty(plates, p):
    n = len(plates)
    k = len(plates[0])
    cache = [[0 for _ in range(p + 1)] for __ in range(n)]
    ret = 0
    for i in range(n):
        stack_sum = 0
        for j in range(min(len(plates[i]) + 1, p + 1)):
            if i == 0:
                cache[i][j] = stack_sum
                ret = max(cache[i][j], ret)
            else:
                # j plates are picked from current stack
                for k in range(0, p - j + 1):
                    cache[i][j + k] = max(cache[i][j + k], cache[i - 1][k] + stack_sum)
                    ret = max(cache[i][j + k], ret)

            if j >= len(plates[i]): break
            stack_sum += plates[i][j]

    return ret


if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for i in range(1, t + 1):
        n, k, p = list(map(int, sys.stdin.readline().split()))
        plates = []
        for _ in range(n):
            plates.append(list(map(int, sys.stdin.readline().split())))
        print(f"Case #{i}: {get_max_beauty(plates, p)}")
