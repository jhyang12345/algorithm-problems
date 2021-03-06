def dfs(graph, cur):
    visited = {}
    stack = []
    stack.append(cur)
    while stack:
        s = stack.pop()
        if s not in visited:
            print(s)
            visited[s] = True
        for node in graph[s]:
            if node not in visited:
                stack.append(node)

# https://www.geeksforgeeks.org/iterative-depth-first-traversal/

graph = {
    1: [2, 3],
    2: [4, 1],
    3: [5, 6, 1],
    4: [2],
    5: [3],
    6: [3],
}

dfs(graph, 1)
