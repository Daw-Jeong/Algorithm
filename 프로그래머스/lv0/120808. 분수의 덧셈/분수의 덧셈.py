from fractions import Fraction
def solution(num1, denom1, num2, denom2):
    answer = Fraction(num1, denom1) + Fraction(num2, denom2)
    return [answer.numerator, answer.denominator]

# import math
# def solution(numer1, denom1, numer2, denom2):
#     tempNumer = numer1 * denom2 + numer2 * denom1
#     tempDenom = denom1 * denom2

#     for i in range(denom1 * denom2, 1, -1):
#         if tempNumer % i == 0 and tempDenom % i == 0 :
#             tempNumer /= i
#             tempDenom /= i
#             break
            
#     answer = [tempNumer, tempDenom]
    
#     return answer

#     tempNumer = numer1 * denom2 + numer2 * denom1
#     tempDenom = denom1 * denom2
    
#     temp = math.gcd(tempNumer, tempDenom)
#     answer = [tempNumer/temp, tempDenom/temp]
    
#     return answer
    
