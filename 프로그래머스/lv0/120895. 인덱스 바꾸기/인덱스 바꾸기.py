def solution(my_string, num1, num2):

    # return my_string[:num1] + my_string[num2] + my_string[num1+1:num2] + my_string[num1] + my_string[num2+1:]
    
    strlist = list(my_string)
    strlist[num1], strlist[num2] = strlist[num2], strlist[num1]
    
    return ''.join(strlist)