import math
def solution(n):
    i = 0
    while math.factorial(i) <= n:
        i += 1
    return i - 1