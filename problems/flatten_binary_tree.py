# Given a binary tree, flatten the binary tree using inorder traversal.
# Instead of creating a new list, reuse the nodes, where the list is
# represented by following each right child. As such the root should always
# be the first element in the list so you do not need to return anything
# in the implementation, just rearrange the nodes such that following the
# right child will give us the list.
#
# Here's an example and some starter code.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.value}, {self.left}, {self.right})"

def flatten_bst(root):
    cur = root
    left = cur.left
    right = cur.right
    cur.left = None
    if left:
        cur.right = flatten_bst(left)
        left = cur.right
        print(left)
    if right:
        if left:
            while left.right:
                left = left.right
            left.right = flatten_bst(right)
        else:
            cur.right = flatten_bst(right)
        # if right:
        #     cur.right.right = flatten_bst(right)
    return cur


n5 = Node(5)
n4 = Node(4)
n3 = Node(3, n4)
n2 = Node(2, n5)
n1 = Node(1, n2, n3)

#      1
#    /   \
#   2     3
#  /     /
# 5     4

flatten_bst(n1)
print(n1)

# n1 should now look like
#   1
#    \
#     2
#      \
#       5
#        \
#         3
#          \
#           4

n4 = Node(6)
n3 = Node(5, None, n4)
n2 = Node(2, Node(3), Node(4))
n1 = Node(1, n2, n3)

#      1
#    /   \
#   2     3
#  /     /
# 5     4

flatten_bst(n1)
print(n1)

# n1 should now look like
#   1
#    \
#     2
#      \
#       5
#        \
#         3
#          \
#           4
