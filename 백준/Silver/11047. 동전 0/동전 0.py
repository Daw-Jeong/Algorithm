import sys
input = sys.stdin.readline
variety, money = map(int, input().split())
count = 0

coin = []
for i in range(variety):
    coin.append(int(input()))

coin.sort(reverse=True)

for c in coin:
    count += money // c
    money %= c

print(count)