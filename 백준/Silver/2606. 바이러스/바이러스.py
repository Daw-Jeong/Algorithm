import sys
input = sys.stdin.readline

n = int(input())
link = int(input())

graph = [[0] * n for _ in range(n)]

for i in range(link):
    com1, com2 = map(int, input().split())
    graph[com1 - 1][com2 - 1] = 1
    graph[com2 - 1][com1 - 1] = 1

visited = [False] * n
li = []

def dfs(N, li, visited):
    li.append(N)
    visited[N] = True
    for i in range(n):
        if graph[N][i] == 1 and not visited[i]:
            dfs(i, li, visited)
    
dfs(0, li, visited)

print(len(li) - 1)