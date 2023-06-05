def solution(sides):
    # max(sides) < min(sides) + n
    # sum(sides) > n    
    return sum(sides) - (max(sides) - min(sides)) - 1