import math
def solution(my_str, n):
    answer = []
    for i in range(0, math.ceil(len(my_str)/n)):
        str = ''
        
        for j in range(0, n):
            idx = i * n + j
            
            if idx > len(my_str) - 1: break
        
            str += my_str[idx]
            
        answer.append(str)
        
    return answer