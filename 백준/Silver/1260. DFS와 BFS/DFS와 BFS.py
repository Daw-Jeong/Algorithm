import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
link = []

for _ in range(M):
    link.append(list(map(int, input().split())))

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in link:
    a, b = i
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def dfs(graph, V, visited):
    visited[V] = True
    print(V, end = ' ')

    for i in graph[V]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, V, visited)

print()

visited = [False] * (N+1)

def bfs(graph, V, visited):
    
    queue = deque()
    queue.append(V)
    visited[V] = True

    while queue:
        V = queue.popleft()
        print(V, end = ' ')

        for i in graph[V]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, V, visited)