import sys

S = int(sys.stdin.readline())

N = 1
while 1:
    if N * (N + 1) // 2 <= S < (N + 1) * (N + 2) // 2:
        break
    N += 1

print(N)