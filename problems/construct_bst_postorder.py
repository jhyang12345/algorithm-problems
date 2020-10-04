# Given a postorder traversal for a binary search tree, reconstruct the tree.
# A postorder traversal is a traversal order where the left child always
# comes before the right child, and the right child always comes before the parent for all nodes.

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.value) + ", " + self.left.__repr__() + ", " + self.right.__repr__() + ")"


def create_actual_tree(postorder, bottom, top):
    if not postorder:
        return None
    cur = postorder[-1]
    root = None
    if bottom < cur < top:
        root = Node(cur)
        postorder.pop()
        root.right = create_actual_tree(postorder, cur, top)
        root.left = create_actual_tree(postorder, bottom, cur)
    return root


def create_tree(postorder):
    return create_actual_tree(postorder, -1, 100000)

# 2 is the root node, with 1 as the left child and 3 as the right child
print(create_tree([1, 3, 2]))

print(create_tree([1, 7, 5, 50, 40, 10]))
