def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        for l in range(i + 1 , len(prices)):
            answer[i] += 1
            if prices[l] >= prices[i]:
                continue
            else:
                break
                
    return answer