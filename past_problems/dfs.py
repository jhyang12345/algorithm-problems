def bfs(graph, visited, cur):
    q = [cur]
    i = 0
    print(graph)
    while i < len(q):
        cur_node = q[i]
        print(cur_node)
        visited[cur_node] = True
        for node in graph[cur_node]:
            if not visited[node]:
                q.append(node)
        i += 1


def dfs(graph, visited, cur):
    visited[cur] = True
    print(cur)
    for node in graph[cur]:
        if not visited[node]:
            dfs(graph, visited, node)

graph_input = [[1, 2], [2, 4], [1, 3], [2, 5], [5, 6]]

def main():
    nodes = 6
    visited = [False for _ in range(nodes + 1)]
    graph = {node: [] for node in range(1, nodes + 1)}
    for pair in graph_input:
        a, b = pair
        graph[a].append(b)
        graph[b].append(a)
    bfs(graph, visited, 1)

if __name__ == '__main__':
    main()