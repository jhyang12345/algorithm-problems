# Given a tree, find if the binary tree is height balanced or not.
# A height balanced binary tree is a tree where every node's 2 subtree do not differ in height by more than 1.

# Here's some starter code:

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_height_balanced(tree):
    queue = [(tree, 1)]
    lowest = -1
    highest = -1
    while queue:
        cur, level = queue.pop(0)
        if not cur.left or not cur.right:
            if lowest == -1:
                lowest = level
            highest = level
        if cur.left:
            queue.append((cur.left, level + 1))
        if cur.right:
            queue.append((cur.right, level + 1))
    print(highest, lowest)
    return highest - lowest < 2

#     1
#    / \
#   2   3
#  /
# 4
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)

print(is_height_balanced(n1))
# True

#     1
#    /
#   2
#  /
# 4
n1 = Node(1, n2)
print(is_height_balanced(n1))
# False
