import sys
input = sys.stdin.readline

INF = 2e9
N, M = map(int, input().split())
graph = [[INF] * N for _ in range(N)]

for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    i, j = map(int, input().split())
    graph[i - 1][j - 1] = 1
    graph[j - 1][i - 1] = 1

def Floyd(graph, N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

Floyd(graph, N)
dist = []
for n in range(N):
    dist.append(sum(graph[n]))

print(dist.index(min(dist)) + 1)