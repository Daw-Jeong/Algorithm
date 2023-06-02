def solution(today, terms, privacies):
    answer = []
    
    #dic으로 약관 종류, 기간 나누기
    termsdic = {}
    for c in terms:
        key, val = c.split()
        termsdic[key] = int(val)
        
    #오늘 날짜 년 월 일 split('.')
    todayY, todayM, todayD = [int(i) for i in today.split('.')]
    
    #for range로(회원번호때문에) privacies if 약관 해서 날짜 구하는 로직
    for i in range(len(privacies)):
        #날짜 구하는 로직 split() 해서 약관 떼고 
        due, priv = privacies[i].split()
        #다시 split('.')해서 년 월 일 구하고
        
        dueY, dueM, dueD = [int(i) for i in due.split('.')]
        
        #일-1 해서 if == 0하면 28 할당 월 -= 1
        if dueD - 1 == 0:
            dueD = 28
            dueM -= 1
        else: dueD -= 1
        
        #월+(약관에 해당하는 기간) 해서 if > 12 하면 -12 * n 해주고 년 += n
        # Y 에서 -1 해주는 이유는 12 // 12 는 1이 되어서 1 더해지니까 -1 해주고 해야 13부터 +1 해준다 
        if (dueM + termsdic[priv]) % 12 != 0:
            dueY += (dueM + termsdic[priv] - 1) // 12
            dueM = (dueM + termsdic[priv]) % 12
        else:
            dueY += (dueM + termsdic[priv] - 1) // 12
            dueM = 12
            
        print(dueY, dueM, dueD)
        

        if todayY < dueY:
            continue
        elif todayY > dueY:
            answer.append(i+1)
        else:
            if todayM < dueM:
                continue
            elif todayM > dueM:
                answer.append(i+1)
            else:
                if todayD > dueD:
                    answer.append(i+1)
                else:
                    continue
                    
    return answer