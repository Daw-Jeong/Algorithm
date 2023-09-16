def solution(s):
    answer = []
    trial = 0
    cnt = 0
    
    while len(s) > 1:
        cnt += s.count('0')
        s = s.replace('0','')
        s = bin(len(s))[2:]
        trial += 1
        
    answer.append(trial)
    answer.append(cnt)
    
    return answer
    
    