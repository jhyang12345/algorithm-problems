# You are given the root of a binary search tree. 
# Return true if it is a valid binary search tree, and false otherwise.
# Recall that a binary search tree has the property that all values in
# the left subtree are less than or equal to the root, and all values in
# the right subtree are greater than or equal to the root.

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def is_bst(root):
    min_right = None
    max_left = None
    if root.left:
        flag, left_max, right_min = is_bst(root.left)
        if not flag:
            return flag, 0, 0
        max_left = left_max
    if root.right:
        flag, left_max, right_min = is_bst(root.right)
        if not flag:
            return flag, 0, 0
        min_right = right_min

    if min_right and max_left:
        if min_right < max_left:
            return False, 0, 0
        if not (max_left < root.key < min_right):
            return False, 0, 0

    if min_right == None:
        min_right = root.key
    if max_left == None:
        max_left = root.key
    print(root.key, max_left, min_right)
    return True, max(max_left, root.key, min_right), min(min_right, max_left, root.key)


a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(is_bst(a))


a = TreeNode(2)
a.left = TreeNode(3)
a.right = TreeNode(1)
print(is_bst(a))


a = TreeNode(4)
a.left = TreeNode(2)
a.right = TreeNode(5)
a.right.left = TreeNode(3)
a.right.right = TreeNode(6)
print(is_bst(a))
