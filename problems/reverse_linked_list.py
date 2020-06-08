class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

  # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    def reverseIteratively(self, head):
        arr = []
        while head != None:
            arr.append(head)
            head = head.next

        for i in range(len(arr) - 1, -1, -1):
            cur = arr[i]
            if i > 0:
                next = arr[i - 1]
            else:
                next = None
            cur.next = next


    # Recursive Solution
    def reverseRecursively(self, head):
        print(head.val)
        if head.next == None:
            return head
        node = self.reverseRecursively(head.next)
        node.next = head
        head.next = None
        return head
# Implement this.

# Test Program
# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseIteratively(testHead)
print("List after reversal: ")
testTail.printList()


# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()

testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4
