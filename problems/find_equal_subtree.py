class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"

def inorder(tree):
    ret = ""
    if tree.left:
        ret += inorder(tree.left)
    ret += str(tree.value)
    if tree.right:
        ret += inorder(tree.right)
    return ret

def preorder(tree):
    ret = ""
    ret += str(tree.value)
    if tree.left:
        ret += inorder(tree.left)
    if tree.right:
        ret += inorder(tree.right)
    return ret

def find_subtree(t, s):
    inorder_t = inorder(t)
    preorder_t = preorder(t)
    print(inorder_t, preorder_t)
    queue = [s]
    while queue:
        cur = queue.pop(0)
        if cur.value == t.value:
            inorder_cur = inorder(cur)
            preorder_cur = preorder(cur)
            if inorder_cur == inorder_t and preorder_cur == preorder_t:
                return True
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return False

t3 = Node(4, Node(3), Node(2))
t2 = Node(5, Node(4), Node(-1))
t = Node(1, t3, t2)

s = Node(4, Node(3), Node(2))
"""
Tree t:
    1
   / \
  4   5
 / \ / \
3  2 4 -1

Tree s:
  4
 / \
3  2
"""

print(find_subtree(s, t))
# True
