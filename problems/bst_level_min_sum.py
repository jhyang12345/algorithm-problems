# You are given the root of a binary tree. Find the level for the binary tree with the minimum sum, and return that value.
#
# For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10, and 4 + 1 + 2 = 7. So, the answer here should be 7.

class Node:
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right

def minimum_level_sum(root):
    level = 1
    queue = [(root, level)]
    dict = {}
    while queue:
        cur, level = queue.pop(0)
        if level not in dict:
            dict[level] = cur.val
        else:
            dict[level] += cur.val
        if cur.left:
            queue.append([cur.left, level + 1])
        if cur.right:
            queue.append([cur.right, level + 1])
    ret = None
    for x in dict:
        if ret == None:
            ret = dict[x]
        else:
            ret = min(dict[x], ret)
    return ret


#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

print(minimum_level_sum(node))
