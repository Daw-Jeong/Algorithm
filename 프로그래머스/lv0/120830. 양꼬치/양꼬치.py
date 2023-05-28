def solution(n, k):
    # 조건엔 이미 k 가 n / 10 보다 같거나 크다고 나와서 0보다 작을지 비교할 필요는 없지만 일반적으로 그 조건 없이 보면 음료수를 할인하는 양보다 적게 먹을 수도 있으니까 max함수로 비교해서!
    
    drink = max(0, k - n // 10)
    
    return 12000 * n + 2000 * drink

#     answer = 0
#     discount = n // 10
#     if k >= discount:
#         answer += (k - discount) * 2000 + 12000 * n
#     else:
#         answer = 12000 * n
    
#     return answer