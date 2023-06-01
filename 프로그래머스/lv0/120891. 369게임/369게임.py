def solution(order):
    clap = ['3', '6', '9']
    order_str = str(order)
    
    return sum([1 for i in order_str if i in clap])