import math
def solution(n):
    count = 0
    # n 이하 자연수 돌면서
    for i in range(1, n + 1):
        # 범위 제곱근까지만 체크해서 약수 있으면 count 늘리고 내부 for문 종료
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0: 
                count += 1
                break
        
    return count