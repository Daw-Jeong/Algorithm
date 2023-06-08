def solution(before, after):
    beforelist = sorted(list(before))
    afterlist = sorted(list(after))
    
    if beforelist == afterlist:
        return 1
    
    return 0