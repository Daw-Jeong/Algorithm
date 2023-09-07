def solution(s):
    answer = 0
    temp = [0]
    
    for i in s:
        if temp[-1] == i:
            temp.pop()
        else:
            temp.append(i)        

    if len(temp) == 1:
        answer = 1 
    
    return answer