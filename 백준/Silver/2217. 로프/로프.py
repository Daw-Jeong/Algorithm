import sys
input = sys.stdin.readline

rope = []
vol = 0

for _ in range(int(input())):
    rope.append(int(input()))

rope.sort()

for i in range(len(rope)):
    vol = max(vol, rope[i] * (len(rope) - i))

print(vol)