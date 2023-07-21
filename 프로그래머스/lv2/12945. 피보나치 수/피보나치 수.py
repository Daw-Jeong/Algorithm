def solution(n):
    temp1 = 0
    temp2 = 1
    sum = 1
    for i in range(3, n + 1):
        temp1 = temp2
        temp2 = sum   
        sum = temp1 + temp2
        
    return sum % 1234567