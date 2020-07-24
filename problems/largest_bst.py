# You are given the root of a binary tree. Find and return the largest subtree of that tree, which is a valid binary search tree.

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        answer = str(self.key)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer

highest = None

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
    global highest
    highest = root
    return True, max(max_left, root.key, min_right), min(min_right, max_left, root.key)

def largest_bst_subtree(root):
    is_bst(root)
    return highest

#     5
#    / \
#   6   7
#  /   / \
# 2   4   9
node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
print(largest_bst_subtree(node))
