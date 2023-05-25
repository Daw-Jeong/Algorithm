# import math
def solution(price):
    price_rates = {500000:0.8, 300000:0.9, 100000:0.95, 0:1}
    for price_range, rate in price_rates.items():
        if price >= price_range: 
            price *= rate
            return int(price)

#     answer = price
#     if price >= 500000:
#         answer = price * 0.8
#     elif price >= 300000:
#         answer = price * 0.9
#     elif price >= 100000:
#         answer = price * 0.95
    
#     # return math.trunc(answer)
#     return int(answer)
