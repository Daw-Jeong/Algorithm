import sys
input = sys.stdin.readline

INF = 1e9
n = int(input())
m = int(input())

bus_map = [[INF] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            bus_map[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    bus_map[a - 1][b - 1] = min(bus_map[a - 1][b - 1], c)

def Floyd(bus_map, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                bus_map[i][j] = min(bus_map[i][j], bus_map[i][k] + bus_map[k][j])

Floyd(bus_map, n)

for el in bus_map:
    for i in el:
        if i >= INF:
            print(0, end = ' ')
        else: print(i, end = ' ')
    print()