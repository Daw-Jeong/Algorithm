def solution(my_string):
    temp = list(my_string)
    tempSet = dict.fromkeys(my_string)
    return ''.join(tempSet)