def solution(s):
    answer = 0
    stack = list(s)
    temp = [0]
    for i in stack:
        if temp[-1] == i:
            temp.pop()
        else:
            temp.append(i)        

    if len(temp) == 1:
        answer = 1 
    
    return answer