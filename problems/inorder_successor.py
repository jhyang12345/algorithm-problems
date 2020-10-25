# Given a node in a binary search tree (may not be the root), f
# ind the next largest node in the binary search tree (also known as an inorder successor).
# The nodes in this binary search tree will also have a parent field to traverse up the tree.
#
# Here's an example and some starter code:

class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"(Value: {self.value}, Left: {self.left}, Right: {self.right})"


def inorder_successor(node):
    if not node.left and not node.right:
        if node.parent:
            return node.parent
    if node.right:
        cur = node.right
        while cur.left:
            cur = cur.left
        return cur
    else:
        if node.parent and node.parent.left == node:
            return node.parent
    return None


tree = Node(3)
tree.left = Node(2)
tree.right = Node(4)
tree.left.parent = tree
tree.right.parent = tree
tree.left.left = Node(1)
tree.left.left.parent = tree.left
tree.right.right = Node(5)
tree.right.right.parent = tree.right
#     3
#    / \
#   2   4
#  /     \
# 1       5
print(inorder_successor(tree.left).value)
# 3
print(inorder_successor(tree.right).value)
# 5
print(inorder_successor(tree).value)
