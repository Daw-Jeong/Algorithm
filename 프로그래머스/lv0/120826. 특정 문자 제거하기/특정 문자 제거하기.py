def solution(my_string, letter):
    
    return ''.join(i for i in my_string if i != letter)
    
    # return my_string.replace(letter, '')
    
    # answer = ''
    # for i in range(len(my_string)):
    #     if my_string[i] != letter:
    #         answer += my_string[i]
    # return answer