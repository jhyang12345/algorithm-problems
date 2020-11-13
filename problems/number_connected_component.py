# Given a list of undirected edges which represents a graph,
# find out the number of connected components.

def dfs(cur, graph, visited):
    visited[cur] = True
    for node in graph[cur]:
        if not visited[node]:
            dfs(node, graph, visited)

def num_connected_components(edges):
    graph = {}
    for edge in edges:
        x, y = edge
        if x not in graph:
            graph[x] = []
        if y not in graph:
            graph[y] = []
        graph[x].append(y)
        graph[y].append(x)
    visited = {}
    for key in graph:
        visited[key] = False
    count = 0
    for key in graph:
        if not visited[key]:
            count += 1
            dfs(key, graph, visited)
    return count

print(num_connected_components([(1, 2), (2, 3), (4, 1), (5, 6)]))
# 2
