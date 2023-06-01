def solution(order):
    # clap = ['3', '6', '9']
    order_str = str(order)
    
    # return sum([1 for i in order_str if i in clap])
    return order_str.count('3') + order_str.count('6') + order_str.count('9')