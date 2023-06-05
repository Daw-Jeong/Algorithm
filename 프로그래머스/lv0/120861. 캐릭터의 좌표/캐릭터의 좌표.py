def solution(keyinput, board):
    limitX, limitY = board[0]//2, board[1]//2
    dict = {'up':(0, 1), 'down':(0, -1), 'right':(1, 0), 'left':(-1, 0)}
    x, y = 0, 0
    
    for key in keyinput:
        dx, dy = dict[key]
        if abs(x + dx) > limitX or abs(y + dy) > limitY:
            continue
        else:
            x += dx
            y += dy
            
    return [x, y]
    
#     answer = [0, 0]

#     for keyin in keyinput:
#         if keyin == 'up':
#             answer[1] += 1
#             if answer[1] > board[1] // 2:
#                 answer[1] = board[1] // 2
#         elif keyin == 'down':
#             answer[1] -= 1
#             if -answer[1] > board[1] // 2:
#                 answer[1] = -(board[1] // 2)
#         elif keyin == 'right':
#             answer[0] += 1
#             if answer[0] > board[0] // 2:
#                 answer[0] = board[0] // 2
#         else:
#             answer[0] -= 1
#             if -answer[0] > board[0] // 2:
#                 answer[0] = -(board[0] // 2)
                
#     return answer