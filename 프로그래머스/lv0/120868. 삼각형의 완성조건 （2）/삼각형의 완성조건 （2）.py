def solution(sides):
    # max(sides[0], sides[1]) < min(sides[0], sides[1]) + n
    # sum(sides) > n    
    return sum(sides) - (max(sides) - min(sides)) - 1