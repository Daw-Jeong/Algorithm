def solution(n):
#     answer = []
    
#     for i in range(1,int(n ** 0.5)+1):
#         if n % i == 0:
#             answer.append(i)
#             if i == n//i: continue
#             answer.append(n//i)
            
#     answer.sort()
    
#     return answer

    return [i for i in range(1, n + 1) if n % i == 0]