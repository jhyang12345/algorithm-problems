# Given a linked list of integers, remove all consecutive nodes that sum up to 0.

# Example:
# Input: 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
# Output: 10

# The consecutive nodes 5 -> -3 -> -3 -> 1 sums up to 0 so that sequence should be removed. 
# 4 -> -4 also sums up to 0 too so that sequence should also be removed.


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    return str(self.value)

def removeConsecutiveSumTo0(temp_node):
  node_dict = {}
  sum_til_now = 0
  node = temp_node
  while node:
    sum_til_now += node.value
    # print(sum_til_now, node_dict.keys())
    if sum_til_now in node_dict:
      start_node = node_dict[sum_til_now]
      # print(node_dict[sum_til_now], node.value, node.next)
      node_dict = {}
      node_dict[sum_til_now] = start_node
      start_node.next = node.next
    else:
      node_dict[sum_til_now] = node
    node = node.next
  return temp_node

node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)

print("\nStarting")
while node:
    print(node.value)
    node = node.next