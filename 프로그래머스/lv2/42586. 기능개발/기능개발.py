import math
def solution(progresses, speeds):
    answer = []
    left_days = [math.ceil((100 - progresses[i])/speeds[i]) for i in range(len(progresses))]
    print(left_days)
    max_el = left_days[0]
    cnt = 0
    for el in left_days:
        if el <= max_el:
            cnt += 1
        else:
            max_el = el
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
        
    return answer