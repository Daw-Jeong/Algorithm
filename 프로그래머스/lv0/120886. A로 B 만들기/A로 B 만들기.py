def solution(before, after):
    beforelist = sorted(before)
    afterlist = sorted(after)
    
    if beforelist == afterlist:
        return 1
    
    return 0