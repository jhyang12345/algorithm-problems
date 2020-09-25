# Given a binary tree and a given node value, return all of the node's cousins.
# Two nodes are considered cousins if they are on the same level of the tree
# with different parents. You can assume that all nodes will have their own unique value.
#
# Here's some starter code:

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def list_cousins(tree, val):
    queue = [(tree, 1)]
    ret = []
    last = False
    while queue:
        cur, level = queue.pop(0)
        if cur.value == val:
            last = True
            continue
        else:
            if ret and ret[-1][1] != level:
                if last:
                    break
                ret = [(cur, level)]
            else:
                ret.append((cur, level))
        if cur.left:
            queue.append((cur.left, level + 1))
        if cur.right:
            queue.append((cur.right, level + 1))
    return [n[0].value for n in ret]


#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print(list_cousins(root, 5))
