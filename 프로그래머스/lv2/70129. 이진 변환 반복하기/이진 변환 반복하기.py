def solution(s):
    answer = []
    trial = 0
    cnt = 0
    while len(s) > 1:
        cnt += s.count('0')
        s = s.replace('0','')
        s = toBinary(s)
        trial += 1
    answer.append(trial)
    answer.append(cnt)
    return answer

def toBinary(num):
    temp = len(num)
    return bin(temp)[2:]
    
    