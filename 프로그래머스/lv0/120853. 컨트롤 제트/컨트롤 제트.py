def solution(s):
#     sum = 0
#     li = s.split(' ')
    
#     for i in range(len(li)):
#         if li[i] != 'Z':
#             sum += int(li[i])
#         else:
#             sum -= int(li[i - 1])            
    
#     return sum

    stack = []
    for i in s.split():
        if i != 'Z':
            stack.append(int(i))
        else:
            stack.pop()
            
    return sum(stack)