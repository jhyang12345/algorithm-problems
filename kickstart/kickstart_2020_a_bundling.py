# Pip has N strings. Each string consists only of letters from A to Z.
# Pip would like to bundle their strings into groups of size K. Each string must belong to exactly one group.
#
# The score of a group is equal to the length of the longest prefix shared by all the strings in that group. For example:
#
# The group {RAINBOW, RANK, RANDOM, RANK} has a score of 2 (the longest prefix is 'RA').
# The group {FIRE, FIREBALL, FIREFIGHTER} has a score of 4 (the longest prefix is 'FIRE').
# The group {ALLOCATION, PLATE, WORKOUT, BUNDLING} has a score of 0 (the longest prefix is '').
# Please help Pip bundle their strings into groups of size K, such that the sum of scores of the groups is maximized.
#
# Input
# The first line of the input gives the number of test cases, T.
# T test cases follow. Each test case begins with a line containing the two integers N and K.
# Then, N lines follow, each containing one of Pip's strings.

import sys

def get_max_sum_of_scores(words, k):
    words.sort()
    ret = 0
    for i in range(0, len(words), k):
        group = words[i:i + k]
        suffix = group[0]
        end = len(suffix)
        for word in group[1:]:
            n = len(word)
            m = len(suffix)
            if n < m:
                suffix = suffix[:n]
            end = len(suffix)
            i = 0
            while i < end:
                if suffix[i] != word[i]:
                    break
                i += 1
            suffix = suffix[:i]
        ret += len(suffix)
    return ret


if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for i in range(1, t + 1):
        n, k = list(map(int, sys.stdin.readline().split()))
        words = []
        for _ in range(n):
            words.append(sys.stdin.readline().strip())
        print(f"Case #{i}: {get_max_sum_of_scores(words, k)}")
