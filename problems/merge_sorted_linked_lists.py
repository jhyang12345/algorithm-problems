 # Merge K Sorted Linked Lists


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer

def merge(lls):
    mindex = -1
    min_value = None
    node_list = []
    while True:
        allNone = True
        for i, l in enumerate(lls):
            if l == None:
                continue
            if min_value == None or l.val < min_value:
                allNone = False
                min_value = l.val
                mindex = i

        if mindex != -1:
            node_list.append(lls[mindex].val)
            lls[mindex] = lls[mindex].next
            min_value = None
            mindex = -1
        if allNone:
            break
    return node_list





a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))
