def solution(babbling):
    cando = ["aya", "ye", "woo", "ma"]
    count = 0
    
    for bab in babbling:

        while len(bab) >= 0:
            
            if len(bab) == 0:
                count += 1
                break          
            elif len(bab) >= 3 and bab[:3] in cando:
                bab = bab[3:]    
            elif len(bab) >=2 and bab[:2] in cando:
                bab = bab[2:]
            else:
                break
                
    return count

