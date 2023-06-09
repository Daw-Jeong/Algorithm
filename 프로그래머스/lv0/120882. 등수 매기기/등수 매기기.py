def solution(score):
    answer = [] 

    average_score = [(score[i][0] + score[i][1])/2 for i in range(len(score))]
    
    sorted_average_score = sorted(average_score, reverse = True)
      
    for el in average_score:
        print
        answer.append(sorted_average_score.index(el) + 1)
        
    return answer