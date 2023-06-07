def solution(board):
    answer = 0
    fix = []
    board_lim = len(board)
    
    # 수정할 이중배열 만들기
    for i in range(len(board)):
        fix.append([])
        fix[i] += [0 for j in range(board_lim)]
        
    # 돌면서 지뢰인 부분 찾아서 주변 위험지역으로 수정해주는 함수 소환
    for n in range(board_lim):
        for m in range(board_lim):
            if board[n][m] == 1:
                fix = dangerarea(n, m, board_lim, fix)
                
     # 보드 전체 개수에서 수정된 위험지역 배열의 위험지역 개수 모두 더한걸 빼서 안전 지대 구하기
    return board_lim * board_lim - sum([x for y in fix for x in y])

def dangerarea(n, m, board_lim, fix):
     # n, m으로 지뢰 인덱스 받아와서 위험지역 다 1인 fix 이중배열 반환
    fix[n][m] = 1
    
     # 지뢰 행 수정 좌우로 끝보다 큰지 여부에 따라 좌우 수정
    if m - 1 >= 0:
        fix[n][m - 1] = 1
    if m + 1 < board_lim:
        fix[n][m + 1] = 1
    
     # 세로 판단. 지뢰 위 행 수정
    if n - 1 >= 0:
        fix[n - 1][m] = 1
        if m - 1 >= 0:
            fix[n - 1][m - 1] = 1       
        if m + 1 < board_lim:
            fix[n - 1][m + 1] = 1
            
     # 세로 판단. 지뢰의 아래 행 수정
    if n + 1 < board_lim:
        fix[n + 1][m] = 1
        if m - 1 >= 0:
            fix[n + 1][m - 1] = 1
        if m + 1 < board_lim:
            fix[n + 1][m + 1] = 1
            
    return fix