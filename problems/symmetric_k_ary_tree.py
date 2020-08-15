# A k-ary tree is a tree with k-children, and a tree is symmetrical if the data of
# the left side of the tree is the same as the right side of the tree.
#
# Here's an example of a symmetrical k-ary tree.
#         4
#      /     \
#     3        3
#   / | \    / | \
# 9   4  1  1  4  9
# Given a k-ary tree, figure out if the tree is symmetrical.


class Node():
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def are_trees_equal(a, b):
    if len(a.children) != len(b.children):
        return False
    for i in range(len(a.children)):
        child_a = a.children[i]
        child_b = b.children[i]
        if not are_trees_equal(child_a, child_b):
            return False
    return a.value == b.value

def is_reflection(a, b):
    queue = [b]
    while queue:
        cur = queue.pop(0)
        cur.children = cur.children[::-1]
        queue = queue + cur.children
    return are_trees_equal(a, b)

def is_symmetric(root):
    start = 0
    end = len(root.children) - 1
    flag = True
    while start < end:
        if start != end:
            flag = (flag and is_reflection(root.children[start], root.children[end]))
        else:
            flag = (flag and is_symmetric(root.children[start]))
        start += 1
        end -= 1
    return flag


tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
print(is_symmetric(tree))
# True
