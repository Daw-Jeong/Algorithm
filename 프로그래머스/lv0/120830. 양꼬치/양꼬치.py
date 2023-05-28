def solution(n, k):
    answer = 0
    discount = n // 10
    if k >= discount:
        answer += (k - discount) * 2000 + 12000 * n
    else:
        answer = 12000 * n
    
    return answer