def solution(prices):
#     answer = [0] * len(prices)
    
#     for i in range(len(prices)):
#         for l in range(i + 1 , len(prices)):
#             answer[i] += 1
#             if prices[l] >= prices[i]:
#                 continue
#             else:
#                 break
                
#     return answer

    stack = []
    answer = [0] * len(prices) #[1, 2, 3, 2, 3]
    for i in range(len(prices)): #0 1 2 3 4
        while stack != [] and stack[-1][1] > prices[i]:
            past, _ = stack.pop() #[2,3]
            answer[past] = i - past #answer[2] = 1
        stack.append([i, prices[i]]) #[ [0,1] [1,2] [3,2] [4,3] ] 
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer