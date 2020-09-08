# Given a directed graph, reverse the directed graph so all directed edges are reversed.
#
# Example:
# Input:
# A -> B, B -> C, A ->C
#
# Output:
# B->A, C -> B, C -> A
# Here's a starting point:

from collections import defaultdict

class Node:
    def __init__(self, value):
        self.adjacent = []
        self.value = value

    def __str__(self):
        return self.value

def reverse_graph(graph):
    new_dict = {}
    for key in graph:
        if key not in new_dict:
            node = Node(key)
            new_dict[key] = node
        else:
            node = new_dict[key]
        for n in graph[key].adjacent:
            if n.value not in new_dict:
                new_dict[n.value] = Node(n.value)
            new_dict[n.value].adjacent.append(node.value)
    return new_dict


a = Node('a')
b = Node('b')
c = Node('c')

a.adjacent += [b, c]
b.adjacent += [c]

graph = {
    a.value: a,
    b.value: b,
    c.value: c,
}

for _, val in reverse_graph(graph).items():
    print(_, val.adjacent)
# []
# ['a', 'b']
# ['a']
