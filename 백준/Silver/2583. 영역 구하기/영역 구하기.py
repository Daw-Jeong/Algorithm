import sys
input = sys.stdin.readline
from collections import deque

M, N, K = map(int, input().split())
block = [list(map(int, input().split())) for _ in range(K)]
li = [[0 for _ in range(N)] for _ in range(M)]
area = []

for xy in block:
    x1, y1, x2, y2 = xy
    for n in range(x1, x2):
        for m in range(y1, y2):
            li[m][n] = 1


def bfs(x, y):
    
    queue = deque()
    queue.append([x, y])
    dx = [0, 0, 0, 1, -1]
    dy = [0, 1, -1, 0, 0]
    cnt = 0

    while queue:
        x, y = queue.popleft()
        for i in range(5):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < N and 0 <= Y < M and li[Y][X] == 0:
                queue.append([X, Y])
                cnt += 1
                li[Y][X] = 1

    area.append(cnt)
    

for m in range(M):
    for n in range(N):
        if li[m][n] == 0:
            bfs(n, m)

area.sort()
print(len(area))

for el in area:
    print(el, end = " ")