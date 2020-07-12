# You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


def deepest(node):
    cur = node
    depth = 1
    while cur.left:
        cur = cur.left
        depth += 1
    return cur, depth

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
