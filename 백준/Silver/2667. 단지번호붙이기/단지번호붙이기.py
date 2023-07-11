import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

li = []
def bfs(i, j, graph):
    q = deque()
    q.append((i, j))
    graph[i][j] = 0
    li.append([])
    li[-1].append((i, j))

    while q:
        x, y = q.popleft()
        
        for n in range(4):
            X = x + dx[n]
            Y = y + dy[n]

            if 0 <= X < N and 0 <= Y < N and graph[X][Y] == 1:
                q.append((X, Y))
                graph[X][Y] = 0
                li[-1].append((X, Y))


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j, graph)

li.sort(key = len)

print(len(li))
for el in li:
    print(len(el))