import sys
input = sys.stdin.readline

start, end = map(int, input().split())
cnt = 0

while end >= 1:
    if end < start:
        cnt = -1
        break
    elif end == start:
        cnt += 1
        break
    elif end % 2 == 0:
        end //= 2
        cnt += 1
    elif end % 10 == 1:
        end = (end - 1) // 10
        cnt += 1
    else:
        cnt = -1
        break

print(cnt)