import sys
input = sys.stdin.readline

N = int(input())

li = []

for _ in range(N):
    li.append(list(map(int, input().split())))

def Floyd(li, N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if li[i][j] == 0 and li[i][k] == 1 and li[k][j] == 1:
                    li[i][j] = 1

Floyd(li, N)

for el in li:
    for l in el:
        print(l, end = ' ')
    print()