def solution(age):
    alpa = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for c in str(age):
        answer += alpa[int(c)]
    
    return answer