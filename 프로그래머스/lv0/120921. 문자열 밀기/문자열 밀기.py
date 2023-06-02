def solution(A, B):
    
#     doubleA = A+A
#     print(doubleA)
#     answer = -1
    
#     for i in range(1, len(A)):
#         idx = doubleA.find(B, len(A) - i)
#         if idx != -1:
#             answer = idx
#             break
        
#     print(answer)
#     if answer > 0:
#         answer = len(A) - answer
        
#     return answer

    answer = -1
    for i in range(0, len(A)):
        if A[len(A)-i:] + A[:len(A)-i] == B:
            return i
    return answer
    