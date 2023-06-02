def solution(my_string):
    
    return eval(my_string)
    # return sum([int(i) for i in my_string.replace('- ','+ -').split(' + ')])
    
#     li = my_string.split()
#     answer = int(li[0])    
#     for i in range(1, len(li) - 1):
#         if li[i] == '+':
#             answer += int(li[i+1])
#         elif li[i] == '-':
#             answer -= int(li[i+1])
    
#     return answer