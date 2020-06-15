# Implement a class for a stack that supports all the regular functions (push, pop)
# and an additional function of max() which returns the maximum element in the stack
# (return None if the stack is empty). Each method should run in constant time.


class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_list = []


    def push(self, val):
        # Fill this in.
        self.stack.append(val)
        if not self.max_list or val > self.max_list[-1]:
            self.max_list.append(val)
        else:
            self.max_list.append(self.max_list[-1])

    def pop(self):
        self.max_list.pop()
        return self.stack.pop()

    def max(self):
        return self.max_list[-1]

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
