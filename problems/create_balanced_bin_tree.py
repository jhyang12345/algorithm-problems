from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        # level-by-level pretty-printer
        nodes = deque([self])
        answer = ''
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value)
            nodes.append(node.left)
            nodes.append(node.right)
        return answer


def createBalancedBST(nums):
    if len(nums) == 1:
        return Node(nums[0])
    elif len(nums) == 0:
        return None
    mid = len(nums) // 2
    cur_node = Node(nums[mid])
    cur_node.left = createBalancedBST(nums[:mid])
    cur_node.right = createBalancedBST(nums[mid + 1:])
    return cur_node

print(createBalancedBST([1, 2, 3, 4, 5, 6, 7]))
