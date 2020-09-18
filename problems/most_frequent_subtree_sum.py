# Given a binary tree, find the most frequent subtree sum.
#
# Example:
#
#    3
#   / \
#  1   -3
#
# The above tree has 3 subtrees. The root node with 3, and the 2 leaf nodes,
# which gives us a total of 3 subtree sums. The root node has a sum of 1 (3 + 1 + -3),
# the left leaf node has a sum of 1, and the right leaf node has a sum of -3.
# Therefore the most frequent subtree sum is 1.
#
# If there is a tie between the most frequent sum, you can return any one of them.
#
# Here's some starter code for the problem:

class Node():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calc_subtree_sum(root, dict):
    sub = 0
    if root.left:
        calc_subtree_sum(root.left, dict)
        sub += root.left.val
    if root.right:
        calc_subtree_sum(root.right, dict)
        sub += root.right.val
    sub += root.val
    if sub not in dict:
        dict[sub] = 1
    else:
        dict[sub] += 1


def most_freq_subtree_sum(root):
    dict = {}
    sub = 0
    calc_subtree_sum(root, dict)
    max_val = 0
    max_char = ''
    for ch in dict:
        if max_val < dict[ch]:
            max_val = dict[ch]
            max_char = ch
    print(max_val, max_char)

root = Node(3, Node(1), Node(-3))
most_freq_subtree_sum(root)
