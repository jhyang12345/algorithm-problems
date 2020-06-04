import heapq, sys

def renew(unvisited, distance):
	for i in range(len(unvisited)):
		unvisited[i][0] = distance[unvisited[i][1]]
	return unvisited

def dijk(s, adj):
#	print s, adj
	distance = {}
	prev = {}
	visited = [False for i in range(len(adj) + 1)]
	for i in adj:
		distance[i] = sys.maxint
	distance[s] = 0
	visited[s] = True
	unvisited = []
	unvisited.append((distance[s], s))
	heapq.heapify(unvisited)
	while(len(unvisited)):
		uv = heapq.heappop(unvisited)
		cur = uv[1]
		visited[cur] = True
		for i in adj[cur]:
			if visited[i]:
				continue
			newDist = adj[cur][i] + distance[cur]
			if newDist < distance[i]:
				distance[i] = newDist
				prev[i] = cur
				heapq.heappush(unvisited, (distance[i], i))
		heapq.heapify(unvisited)
#	print prev
	ret = []
#	print distance
	for i in distance:
		if i != s and visited[i]:
			ret.append(distance[i])
		elif not visited[i]:
			ret.append(-1)
	return " ".join(map(str,ret))
	

def main():
	cases = int(sys.stdin.readline())
	for i in range(cases):
		ve = map(int, sys.stdin.readline().split())
		v = ve[0]
		e = ve[1]
		adj = {}
		for c in range(1, v+1):
			adj[c] = {}
		for c in range(e):
			p = map(int, sys.stdin.readline().split())
			if p[1] in adj[p[0]]:
				if adj[p[0]][p[1]] < p[2]:
					adj[p[0]][p[1]] = adj[p[0]][p[1]]
				else:
					adj[p[0]][p[1]] = p[2]
			else:
				adj[p[0]][p[1]] = p[2]
			if p[0] in adj[p[1]]:
				if adj[p[1]][p[0]] < p[2]:
					adj[p[1]][p[0]] = adj[p[1]][p[0]]
				else:
					adj[p[1]][p[0]] = p[2]
			else:
				adj[p[1]][p[0]] = p[2]
		s = int(sys.stdin.readline())
		print dijk(s, adj)
		
if __name__ == '__main__':
	main()