class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def largest_path_sum(tree):
    max_val = 0
    max_path = None
    queue = [(tree, tree.value, [tree.value])]
    while queue:
        node, s, path = queue.pop(0)
        max_val = max(max_val, s)
        if s == max_val:
            max_path = path
        if s == max_val:
            max_node = node
        if node.left:
            queue.append((node.left, s + node.left.value, path + [node.left.value]))
        if node.right:
            queue.append((node.right, s + node.right.value, path + [node.right.value]))
    return max_path


tree = Node(1)
tree.left = Node(3)
tree.right = Node(2)
tree.right.left = Node(4)
tree.left.right = Node(5)
#    1
#  /   \
# 3     2
#  \   /
#   5 4
print(largest_path_sum(tree))
# [1, 3, 5]
