class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def valuesAtHeight(root, height):
    queue = [(root, 1)]
    ret = []
    while queue:
        node, h = queue.pop(0)
        if h == height:
            ret.append(node.value)
        if node.left:
            queue.append((node.left, h + 1))
        if node.right:
            queue.append((node.right, h + 1))
    return ret

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(valuesAtHeight(a, 3))
