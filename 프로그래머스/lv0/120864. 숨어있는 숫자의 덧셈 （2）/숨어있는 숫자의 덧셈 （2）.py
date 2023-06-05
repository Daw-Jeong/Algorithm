def solution(my_string):
    
    # for i in range(len(my_string)):
    #     if my_string[i].isalpha():
    #         my_string = my_string.replace(my_string[i], ' ')
    intstr = ''.join(i if i.isdigit() else ' ' for i in my_string)
    
    return sum([int(i) for i in intstr.split()])
