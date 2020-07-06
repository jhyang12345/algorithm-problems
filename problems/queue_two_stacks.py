class Queue:
  def __init__(self):
    self.stack_in = []
    self.stack_out = []

  def enqueue(self, val):
    self.stack_in.append(val)

  def dequeue(self):
    if self.stack_out:
        return self.stack_out.pop()
    while self.stack_in:
        self.stack_out.append(self.stack_in.pop())
    return self.stack_out.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
q.enqueue(5)
q.enqueue(6)
print(q.dequeue())
print(q.dequeue())
q.enqueue(7)
print(q.dequeue())
print(q.dequeue())
