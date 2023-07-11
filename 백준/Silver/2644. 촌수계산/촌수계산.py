import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
family_graph = [[0] * n for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    family_graph[x - 1][y - 1] = 1
    family_graph[y - 1][x - 1] = 1

p1 -= 1
p2 -= 1
def bfs(p1, p2):
    q = deque()
    q.append(p1)
    visited = [False] * n
    visited[p1] = True

    while q:
        v = q.popleft()   
        if v == p2:
            break
        else:
            for i in range(n):
                if not visited[i] and family_graph[v][i] != 0:
                    q.append(i)
                    family_graph[p1][i] = family_graph[p1][v] + 1
                    family_graph[i][p1] = family_graph[p1][v] + 1
                    visited[i] = True
bfs(p1, p2)

# for el in family_graph:
#     print(el)

print(family_graph[p1][p2] if family_graph[p1][p2] != 0 else -1)