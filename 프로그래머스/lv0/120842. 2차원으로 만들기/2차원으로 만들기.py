def solution(num_list, n):
    answer = []
    
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    
#     order = 0
    
#     for i in range(len(num_list)//n):
#         answer.append([])
        
#         for j in range(n):
#             answer[i].append(num_list[order])
#             order += 1
        
    return answer