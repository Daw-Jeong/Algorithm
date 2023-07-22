from collections import deque
def solution(s):
    q = deque(s)
    cntleft = 0
    cntright = 0
    while q:
        temp = q.popleft()
        
        if temp == '(':
            cntleft += 1
        else:
            cntright += 1
        
        if cntleft < cntright:
            return False
               
    if cntleft != cntright:
        return False
    
    return True