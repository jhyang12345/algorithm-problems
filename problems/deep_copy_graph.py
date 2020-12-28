# Given a node in a connected directional graph, create a copy of it.
#
# Here's an example and some starter code.

class Node:
    def __init__(self, value, adj=None):
        self.value = value
        self.adj = adj

        # Variable to help print graph
        self._print_visited = set()
        if self.adj is None:
            self.adj = []

  # Able to print graph
    def __repr__(self):
        if self in self._print_visited:
            return ''
        else:
            self._print_visited.add(self)
            final_str = ''
            for n in self.adj:
                final_str += f'{n}\n'

            self._print_visited.remove(self)
            return final_str + f'({self.value}, ({[n.value for n in self.adj]}))'

def deep_copy_graph(graph_node, visited=None):
    dummy_node = Node(0)
    queue = [graph_node, dummy_node]
    graph = {}
    visited = [graph_node, dummy_node]
    dummy_map = {}
    while queue:
        cur = queue.pop(0)
        dummy = queue.pop(0)
        dummy_map[cur] = dummy
        dummy.value = cur.value
        visited.append(cur)
        for node in cur.adj:
            if node not in visited:
                queue.append(node)
                new_dummy = Node(0)
                queue.append(new_dummy)
                dummy.adj.append(new_dummy)
            else:
                dummy.adj.append(dummy_map[node])
    return dummy_node

n5 = Node(5)
n4 = Node(4)
n3 = Node(3, [n4])
n2 = Node(2)
n1 = Node(1, [n5])
n5.adj = [n3]
n4.adj = [n3, n2]
n2.adj = [n4]
graph_copy = deep_copy_graph(n1)
print(graph_copy)
# (2, ([4]))
# (4, ([3, 2]))
# (3, ([4]))
# (5, ([3]))
# (1, ([5]))
