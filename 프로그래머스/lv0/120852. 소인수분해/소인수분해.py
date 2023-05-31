def solution(n):
    #n 이하 소수 인덱스에 True인 리스트 만들기 위해 0~n인덱스 True 리스트 초기 선언
    p_num_bool= [True for i in range(n + 1)]
    
    # n의 제곱근까지 범위 내에 소수 찾기
    for i in range(2, int(n ** 0.5) + 1):
        # 2부터 자기 자신 제외한 배수 False 할당
        if p_num_bool[i] == True:
            j = 2 
            #자기 자신 제외 위해 2 곱한 것부터
            while i * j <= n:
                p_num_bool[i * j] = False
                j += 1
    #소수 즉 True로 해둔 인덱스 숫자들을 리스트로
    p_num = [idx for idx, bool in enumerate(p_num_bool) if bool == True]
    
    # 0, 1 은 소수 아니니 제거
    del p_num [:2]
    
    # 소인수 리스트(중복 없이)
    answer = []
    
    #sort 안해도 처음부터 오름차순이어서 그대로
    for i in p_num:
        if n % i == 0:
            answer.append(i)
            

    return answer

