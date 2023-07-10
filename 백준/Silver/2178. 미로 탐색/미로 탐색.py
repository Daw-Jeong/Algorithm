import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):
    #여기서 .rstrip() 은 우측 공백 제거
    graph.append(list(map(int, input().rstrip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph, i, j):

    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        
        for i in range(4):
                X = x + dx[i]
                Y = y + dy[i]

                if 0 <= X < N and 0 <= Y < M and graph[X][Y] == 1:
                    q.append((X, Y))
                    graph[X][Y] = graph[x][y] + 1

    return graph[N-1][M-1]

print(bfs(graph, 0, 0))