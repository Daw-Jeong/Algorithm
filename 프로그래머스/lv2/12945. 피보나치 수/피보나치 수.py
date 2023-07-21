def solution(n):
    temp1 = 0
    temp2 = 1
    for _ in range(2, n + 1):
        temp1, temp2 = temp2, temp1 + temp2
        
    return temp2 % 1234567