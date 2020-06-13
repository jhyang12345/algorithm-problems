# Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    cur_node = root_node
    last_node = cur_node
    going_left = False
    while cur_node != None:
        last_node = cur_node
        if cur_node.value < k and not going_left:
            cur_node = cur_node.right
        elif cur_node.value > k:
            cur_node = cur_node.left
            going_left = True
        else:
            break
    print(last_node.value)
    cur_node = root_node
    last_node = cur_node
    going_right = False
    while cur_node != None:
        last_node = cur_node
        if cur_node.value < k:
            cur_node = cur_node.right
            going_right = True
        elif cur_node.value > k and not going_right:
            cur_node = cur_node.left
        else:
            break
    print(last_node.value)

root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

findCeilingFloor(root, 5)
