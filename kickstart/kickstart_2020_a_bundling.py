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

class Trie:
    def __init__(self, char):
        self.char = char
        self.length = 0
        self.count = 1
        self.children = {}

    def add(self, char):
        node = None
        if char in self.children:
            node = self.children[char]
            node.count += 1
        else:
            node = Trie(char)
            self.children[char] = node
        node.length = self.length + 1
        return node

    def __str__(self):
        return f"{self.count} {self.children.keys()}"

def dfs(root, k):
    s = 0
    value = 0
    for key in root.children:
        node, count, v = dfs(root.children[key], k)
        s += count
        value += v
    count = 0
    root.count -= s

    if root.count >= k:
        remainder = root.count % k
        count = root.count - remainder
        value += root.length
    return root, count + s, value

def get_max_sum_of_scores(words, k):
    root = Trie(None)
    for word in words:
        next = root
        for ch in word:
            next = next.add(ch)
    _, _, value = dfs(root, k)
    return value

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for i in range(1, t + 1):
        n, k = list(map(int, sys.stdin.readline().split()))
        words = []
        for _ in range(n):
            words.append(sys.stdin.readline().strip())
        print(f"Case #{i}: {get_max_sum_of_scores(words, k)}")
