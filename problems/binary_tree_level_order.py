# Given the root of a binary tree, print its level-order traversal. For example:
#
#   1
#  / \
# 2   3
#    / \
#   4   5
#
# The following tree should output 1, 2, 3, 4, 5.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_level_order(root):
    queue = [root]
    while queue:
        cur = queue.pop(0)
        print(cur.val)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
            

root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(root)
# 1 2 3 4 5
