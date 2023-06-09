def solution(numlist, n):
    sorted_numlist = sorted(numlist, reverse = True)
    temp = [[abs(val-n),idx] for idx, val in enumerate(sorted_numlist)]
    temp.sort()
    answer = [sorted_numlist[i[1]] for i in temp]
    
    return answer