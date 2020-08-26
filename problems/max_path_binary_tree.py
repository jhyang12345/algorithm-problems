# You are given the root of a binary tree. Find the path between 2 nodes
# that maximizes the sum of all the nodes in the path, and return the sum.
# The path does not necessarily need to go through the root.
# https://www.geeksforgeeks.org/find-maximum-path-sum-two-leaves-binary-tree/

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxPathSum(root):
    ret = root.val
    max_value = root.val
    left = 0
    right = 0
    if root.left:
        r, m = maxPathSum(root.left)
        left = root.val + r
        max_value = max(max_value, m)
        ret = max(ret, left)
    if root.right:
        r, m = maxPathSum(root.right)
        right = root.val + r
        max_value = max(max_value, m)
        ret = max(ret, right)
    max_value = max(max_value, ret)
    max_value = max(max_value, right + left - root.val)
    return ret, max_value

# (* denotes the max path)
#       *10
#       /  \
#     *2   *10
#     / \     \
#   *20  1    -25
#             /  \
#            3    4
root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
print(maxPathSum(root)[-1])
# 42


root = Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right= Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)
root.right.right.right.right.left = Node(10)
print(maxPathSum(root)[-1])
