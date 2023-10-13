#bfs

import sys
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    que = deque()
    que.append((0, 0))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while que:
        (x, y) = que.popleft()
        
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            
            if 0 <= X < n and 0 <= Y < m and maps[X][Y] == 1:
                que.append((X, Y))
                maps[X][Y] = maps[x][y] + 1
                                                         
            
    if maps[n - 1][m - 1] == 1:
        return -1
    else:
        return maps[n - 1][m - 1]
