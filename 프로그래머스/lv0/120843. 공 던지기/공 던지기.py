def solution(numbers, k):

#     answer = -1
#     for i in range(1, k+1):
#         answer += 2
#         if answer > len(numbers):
#             answer -= len(numbers)
        
#     return answer

    return 2 * (k - 1) % len(numbers) + 1