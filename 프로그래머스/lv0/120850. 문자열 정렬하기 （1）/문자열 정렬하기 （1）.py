def solution(my_string):

    # return sorted([int(i) for i in my_string if i in "0123456789"])
    return sorted([int(i) for i in my_string if i.isdigit()])