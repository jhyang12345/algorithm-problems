# A number can be constructed by a path from the root to a leaf.
# Given a binary tree, sum all the numbers that can be constructed
# from the root to all leaves.
#
# Here's an example and some starter code.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"


def bst_numbers_sum(root, num=0):
    queue = [root]
    ret = 0
    while queue:
        cur = queue.pop(0)
        if not cur.left and not cur.right:
            ret += cur.value
        else:
            if cur.left:
                cur.left.value += cur.value * 10
                queue.append(cur.left)
            if cur.right:
                cur.right.value += cur.value * 10
                queue.append(cur.right)
    return ret


n5 = Node(5)
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4, n5)
n1 = Node(1, n2, n3)

#      1
#    /   \
#   2     3
#  / \
# 4   5

print(bst_numbers_sum(n1))
# 262
# Explanation: 124 + 125 + 13 = 262
