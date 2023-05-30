def solution(my_string):
    
    for i in range(len(my_string)):
        if my_string[i].islower():
            my_string = my_string[:i] + my_string[i].upper() + my_string[i+1:]
        else:
            my_string = my_string[:i] + my_string[i].lower() + my_string[i+1:]
            
    return my_string