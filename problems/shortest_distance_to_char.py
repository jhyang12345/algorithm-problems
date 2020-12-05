# Given a string s and a character c, find the distance for all characters
# in the string to the character c in the string s. You can assume that the
# character c will appear at least once in the string.
#
# Here's an example and some starter code:
from collections import defaultdict


def shortest_dist(s, c):
    ret = [len(s)] * len(s)
    last = None
    for i in range(len(s)):
        cur = s[i]
        if cur == c:
            ret[i] = 0
            last = i
            continue
        else:
            if last != None:
                ret[i] = min(ret[i], i - last)
    last = None
    for i in range(len(s) - 1, -1, -1):
        cur = s[i]
        if cur == c:
            ret[i] = 0
            last = i
            continue
        else:
            if last != None:
                ret[i] = min(ret[i], last - i)
    return ret



print(shortest_dist('helloworld', 'l'))
# [2, 1, 0, 0, 1, 2, 2, 1, 0, 1]
