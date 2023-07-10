def solution(n, s):
    answer = []
    if s < n:
        return [-1]

    
    while s != 0:
        temp = s // n
        answer.append(temp)
        s -= temp
        n -= 1

    return answer
