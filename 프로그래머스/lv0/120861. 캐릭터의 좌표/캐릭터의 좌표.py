def solution(keyinput, board):
    answer = [0, 0]

    for keyin in keyinput:
        if keyin == 'up':
            answer[1] += 1
            if answer[1] > board[1] // 2:
                answer[1] = board[1] // 2
        elif keyin == 'down':
            answer[1] -= 1
            if -answer[1] > board[1] // 2:
                answer[1] = -(board[1] // 2)
        elif keyin == 'right':
            answer[0] += 1
            if answer[0] > board[0] // 2:
                answer[0] = board[0] // 2
        else:
            answer[0] -= 1
            if -answer[0] > board[0] // 2:
                answer[0] = -(board[0] // 2)

                
    return answer