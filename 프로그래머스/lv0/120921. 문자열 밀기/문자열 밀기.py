def solution(A, B):
    answer = -1
    for i in range(0, len(A)):
        if A[len(A)-i:] + A[:len(A)-i] == B:
            return i
    return answer