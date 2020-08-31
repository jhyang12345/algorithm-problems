# You are given a doubly linked list. Determine if it is a palindrome.

class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None

def is_palindrome(node):
    queue = []
    while node:
        queue.append(node.val)
        node = node.next
    n = len(queue)
    if n % 2 == 0:
        stack = queue[:n // 2]
        for x in queue[n//2:]:
            if x == stack[-1]:
                stack.pop()
            else:
                return False
        if not stack:
            return True
    else:
        stack = queue[:n // 2]
        for x in queue[n//2 + 1:]:
            if x == stack[-1]:
                stack.pop()
            else:
                return False
        if not stack:
            return True

node = Node('a')
node.next = Node('b')
node.next.prev = node
node.next.next = Node('b')
node.next.next.prev = node.next
node.next.next.next = Node('a')
node.next.next.next.prev = node.next.next

# True
print(is_palindrome(node))
