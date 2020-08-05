class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def arith(op, a, b):
    if op == PLUS:
        return a + b
    elif op == MINUS:
        return a - b
    elif op == TIMES:
        return a * b
    elif op == DIVIDE:
        return a / b

def evaluate(root):
    if root.val not in [PLUS, MINUS, TIMES, DIVIDE]:
        return root.val
    else:
        return arith(root.val, evaluate(root.left), evaluate(root.right))


tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))
