def solution(quiz):
    answer = []
    
    for express in quiz:
        exp, result = express.split('=')
        answer.append("O") if eval(exp) == int(result) else answer.append("X")
        
    return answer
    
#     answer = []
    
#     for express in quiz:
#         X, oper, Y, eq, Z = express.split()
        
#         if oper == '+':
#             result = 1 if int(X) + int(Y) == int(Z) else 0
#         else:
#             result = 1 if int(X) - int(Y) == int(Z) else 0
            
#         if result:
#             answer.append("O")
#         else:
#             answer.append("X")
    
#     return answer