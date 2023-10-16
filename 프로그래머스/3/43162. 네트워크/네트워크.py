#dfs
def dfs(v, visited, computers, li):
    if not visited[v]:
        visited[v] = True
        for i in range(len(computers)):
            if computers[v][i] == 1:
                li[-1].append(i)
                dfs(i, visited, computers, li)

def solution(n, computers):
    visited = [False for i in range(n)]
    li = []
    for l in range(n):
        if not visited[l]:
            li.append([])
            dfs(l, visited, computers, li)
    
    return len(li)
