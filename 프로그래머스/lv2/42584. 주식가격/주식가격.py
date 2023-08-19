def solution(prices):
    answer = [0 for _ in range(len(prices))]
    
    for i in range(len(prices)):
        temp = prices[i]
        for l in range(i + 1 , len(prices)):
            if prices[l] < temp:
                answer[i] = l - i
                break
            else:
                answer[i] = len(prices) - 1 - i
                
    return answer