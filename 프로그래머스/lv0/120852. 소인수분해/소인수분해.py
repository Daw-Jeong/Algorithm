def solution(n):
    li = []
    i = 2
    
    while n >= i:
        if n % i == 0:
            n /= i
            li.append(i)
            # if i not in li:
            #     li.append(i)
        else:
            i += 1
    answer = dict.fromkeys(li)
    return list(answer)

#     #n 이하 소수 인덱스에 True인 리스트 만들기 위해 0~n인덱스 True 리스트 초기 선언
#     is_prime= [True for i in range(n + 1)]
    
#     #0,1은 소수 아니니 False 할당
#     is_prime[0], is_prime[1] = False, False
    
#     # 범위 내에 소수 찾기
#     for i in range(2, int(n ** 0.5) + 1):
        
#         # 2부터 자기 자신 제외한 배수 False 할당
#         if is_prime[i] == True:
#             j = 2 
#             #자기 자신 제외 위해 2 곱한 것부터
#             while i * j <= n:
#                 is_prime[i * j] = False
#                 j += 1
                
#     #소수, 즉 True로 해둔 인덱스 숫자들을 리스트로
#     prime = [idx for idx, bool in enumerate(is_prime) if bool == True]   
    
#     # 소인수 리스트(중복 없이)
#     answer = []
    
#     #sort 안해도 처음부터 오름차순이어서 그대로
#     for i in prime:
#         if n % i == 0:
#             answer.append(i)            

#     return answer

