# https://www.acmicpc.net/problem/16234
# N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며,
# r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다.
# 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.
#
# 오늘부터 인구 이동이 시작되는 날이다.
#
# 인구 이동은 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.
#
# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.
# 각 나라의 인구수가 주어졌을 때, 인구 이동이 몇 번 발생하는지 구하는 프로그램을 작성하시오.


import sys
from collections import defaultdict

n, l, r = list(map(int, sys.stdin.readline().split()))

def bfs_all(graph, l, r):
    n = len(graph)
    m = len(graph[0])
    visited = defaultdict(int)
    change = 0
    groups = []
    for i in range(n):
        for j in range(m):
            cur = (i, j)
            if not visited[cur]:
                cur_group = []
                cur_sum = 0
                queue = [cur]
                # print("NEW")
                while queue:
                    x, y = queue.pop(0)
                    if visited[(x, y)]:
                        continue
                    visited[(x, y)] = 1
                    cur_group.append((x, y))
                    x_s = []
                    y_s = []
                    if x > 0:
                        x_s.append(-1)
                    if x < (n - 1):
                        x_s.append(1)
                    if y > 0:
                        y_s.append(-1)
                    if y < (m - 1):
                        y_s.append(1)
                    for a in x_s:
                        if not visited[(x + a, y)] and l <= abs(graph[x][y] - graph[x + a][y]) <= r:
                            queue.append((x + a, y))
                    for b in y_s:
                        if not visited[(x, y + b)] and l <= abs(graph[x][y] - graph[x][y + b]) <= r:
                            queue.append((x, y + b))
                groups.append(cur_group)
    for group in groups:
        cur_sum = 0
        for x, y in group:
            cur_sum += graph[x][y]
        indi = cur_sum // len(group)
        for x, y in group:
            if graph[x][y] != indi:
                change += 1
            graph[x][y] = indi
    if not change:
        return False
    return True


graph = []
for _ in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    graph.append(arr)
count = 0
while bfs_all(graph, l, r):
    count += 1
print(count)
