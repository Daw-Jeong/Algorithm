def solution(score):
    sum_score = [sum(score[i]) for i in range(len(score))]
    sorted_score = sorted(sum_score, reverse = True)
          
    return [sorted_score.index(el) + 1 for el in sum_score]