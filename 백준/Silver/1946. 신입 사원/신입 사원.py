import sys
input = sys.stdin.readline

total_case = int(input())

for _ in range(total_case):
    total_apply = int(input())
    score = []
    for _ in range(total_apply):
        score.append(list(map(int, input().split())))
    score.sort()
    minrank = score[0][1]
    failed = 0
    for el in score:
        if el[1] <= minrank:
            minrank = el[1]
        else:
            failed += 1

    print(len(score) - failed)