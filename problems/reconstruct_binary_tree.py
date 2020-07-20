from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            n = q.popleft()
            result += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return result


def reconstruct(preorder, inorder):
    root = preorder[0]
    index = inorder.index(root)
    left_tree = inorder[:index]
    right_tree = inorder[index + 1:]
    left_start = -1
    right_start = -1
    for x in preorder[1:]:
        if x in left_tree and left_start == -1:
            left_start = preorder.index(x)
        if x in right_tree and right_start == -1:
            right_start = preorder.index(x)
    left = None
    right = None
    if left_start != -1:
        left = reconstruct(preorder[left_start:], left_tree)
    if right_start != -1:
        right = reconstruct(preorder[right_start:], right_tree)
    print(left, root, right)

    return root

tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                   ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
print(tree)
