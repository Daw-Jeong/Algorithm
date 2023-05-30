def solution(numbers):
#     dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
#     to_num = ''
    
#     while len(numbers) > 0:
#         for num in dic:
#             if numbers.startswith(num):
#                 to_num += dic[num]
#                 numbers = numbers[len(num):]
                
#     return int(to_num)

    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for idx, val in enumerate(arr):
        numbers = numbers.replace(val, str(idx))
        
    return int(numbers)