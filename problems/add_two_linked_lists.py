# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def get_actual_number(self, l):
        val = 0
        power = 1
        cur = l
        while cur:
            val += cur.val * power
            cur = cur.next
            power *= 10
        return val

    def get_list_from_number(self, number):
        num_list = []
        while number >= 1:
            num_list.append(number % 10)
            number //= 10
        ll = ListNode(num_list[0])
        original = ll
        for num in num_list[1:]:
            ll.next = ListNode(num)
            ll = ll.next
        return original

    def addTwoNumbers(self, l1, l2, c = 0):
        number = self.get_actual_number(l1) + self.get_actual_number(l2)
        print(number)
        ll = self.get_list_from_number(number)
        return ll
    # Fill this in.

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
