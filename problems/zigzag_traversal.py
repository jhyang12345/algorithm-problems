# Given a binary tree, return the list of node values in zigzag order traversal. Here's an example

# Input:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#
# Output: [1, 3, 2, 4, 5, 6, 7]

# Here's some starter code

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def zigzag_order(tree):
    queue = [(tree, 1)]
    flag = False
    last_level = 1
    ret = []
    temp_queue = []
    while queue:
        node, level = queue.pop(0)
        ret.append(node.value)
        if last_level != level:
            flag = not flag
        if not flag:
            if node.left:
                temp_queue.append((node.left, level + 1))
            if node.right:
                temp_queue.append((node.right, level + 1))
        else:
            if node.right:
                temp_queue.append((node.right, level + 1))
            if node.left:
                temp_queue.append((node.left, level + 1))
        if not queue:
            queue = queue + temp_queue[::-1]
            temp_queue = []
        last_level = level
    return ret


n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)

print(zigzag_order(n1))
# [1, 3, 2, 4, 5, 6, 7]
