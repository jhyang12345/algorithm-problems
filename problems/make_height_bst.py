# Given a sorted list, create a height balanced binary search tree,
# meaning the height differences of each node can only differ by at most 1.
#
# Here's some code to start with:

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        answer = str(self.value)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer

def create_height_balanced_bst(nums):
    if not nums:
        return None
    n = len(nums)
    mid = n // 2
    value = nums[mid]
    node = Node(value)
    node.left = create_height_balanced_bst(nums[:mid])
    node.right = create_height_balanced_bst(nums[mid + 1:])
    return node


tree = create_height_balanced_bst([1, 2, 3, 4, 5, 6, 7, 8])
print(tree)
# 53214768
#  (pre-order traversal)
#       5
#      / \
#     3    7
#    / \  / \
#   2   4 6  8
#  /
# 1
