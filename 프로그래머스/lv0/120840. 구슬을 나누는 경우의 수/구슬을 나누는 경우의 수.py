# import math
def solution(balls, share):
    
    # return math.factorial(balls)/(math.factorial(balls - share) * math.factorial(share))
    
    return factorial(balls) / (factorial(balls - share) * factorial(share))

    
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result