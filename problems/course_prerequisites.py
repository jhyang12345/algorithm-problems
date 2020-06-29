def dfs(cur, graph, visited, stack):
    visited[cur] = True
    print(cur)
    for n in graph[cur]:
        if not visited[n]:
            dfs(n, graph, visited, stack)
    stack.append(cur)

graph = {
  'CSC300': ['CSC100', 'CSC200'],
  'CSC200': ['CSC100'],
  'CSC100': []
}

visited = {
    key: False for key in graph.keys()
}

stack = []

for n in visited.keys():
    if not visited[n]:
        dfs(n, graph, visited, stack)

print(stack)
