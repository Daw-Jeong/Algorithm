def solution(polynomial):
    li = polynomial.split(' + ')
    frontX = 0
    constantN = 0
    answer = ''
    
    for i in li:
        if i.endswith('x'):
            if i[0] == 'x':
                frontX += 1
            else:
                frontX += int(i[0:-1])
                
        else:
            constantN += int(i)
            
    
    if frontX == 1:
        answer += 'x'
    elif frontX != 0:
        answer += str(frontX) + 'x'
    
    if constantN != 0 and answer != '':
        answer += ' + ' + str(constantN)
    elif constantN != 0 and answer == '':
        answer += str(constantN)
        
    return answer
