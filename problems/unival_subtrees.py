# A unival tree is a tree where all the nodes have the same value. Given a binary tree, return the number of unival subtrees in the tree.
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
# The 5 trees are:
# - The three single '1' leaf nodes. (+3)
# - The single '0' leaf node. (+1)
# - The [1, 1, 1] tree at the bottom. (+1)

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

cache = {}

def tree_value(node):
    if node in cache:
        return node
    cur = node.val
    left = node.left
    right = node.right
    if left:
        if tree_value(left) != cur:
            return -1
    if right:
        if tree_value(right) != cur:
            return -1
    return cur

def count_unival_subtrees(root):
    queue = [root]
    count = 0
    while queue:
        cur = queue.pop(0)
        if tree_value(cur) != -1:
            count += 1
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return count

a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(count_unival_subtrees(a))


a = Node(0)
a.left = Node(0)
a.right = Node(0)

print(count_unival_subtrees(a))
