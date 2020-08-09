# Design a simple stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
# https://leetcode.com/problems/min-stack/discuss/747181/Clear-Python-code-faster-than-96

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.currentMin = float('inf')
        self.prevMins = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x <= self.currentMin:
            self.prevMins.append(self.currentMin)
            self.currentMin = x
        print(self.stack)
        print(self.currentMin)
        print(self.prevMins)

    def pop(self) -> None:
        if self.stack[-1] == self.currentMin:
            self.currentMin = self.prevMins.pop()
        self.stack.pop()
        print(self.stack)
        print(self.currentMin)
        print(self.prevMins)

    def top(self) -> int:
        print(self.stack)
        print(self.currentMin)
        print(self.prevMins)
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.stack)
        print(self.currentMin)
        print(self.prevMins)
        return self.currentMin


x = MinStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
print()
# -3
x.pop()
print(x.top())
print()
# 0
print(x.getMin())
print()
