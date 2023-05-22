def solution(numer1, denom1, numer2, denom2):
    tempNumer = numer1 * denom2 + numer2 * denom1
    tempDenom = denom1 * denom2

    for i in range(denom1 * denom2, 1, -1):
        if tempNumer % i == 0 and tempDenom % i == 0 :
            tempNumer /= i
            tempDenom /= i       
            
    answer = [tempNumer, tempDenom]
    
    return answer