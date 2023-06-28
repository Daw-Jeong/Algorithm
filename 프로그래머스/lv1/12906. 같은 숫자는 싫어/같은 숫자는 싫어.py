# def solution(arr):
#     answer = []
#     for i in arr:
#         if len(answer) == 0:
#             answer.append(i)
#         elif answer[-1] != i:
#             answer.append(i)
#     return answer

def solution(s):
    a = []
    for i in s:
        if a[-1:] != [i]:
            a.append(i)
    return a