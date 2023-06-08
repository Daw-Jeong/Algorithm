import sys
input = sys.stdin.readline

total = int(input())

def solution():
    N, M = map(int, input().split())
    for l in range(M):
        input()
    return N - 1

for i in range(total):
    print(solution())