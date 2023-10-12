def solution(numbers, target):
    answer = recursion(numbers, -1, 0, target)
    return answer

def recursion(numbers, idx, result, target):
    idx += 1
    
    if idx < len(numbers):
        cnt1 = recursion(numbers, idx, result + numbers[idx], target)
        cnt2 = recursion(numbers, idx, result - numbers[idx], target)
        return cnt1 + cnt2
        
    else:
        if result == target:
            return 1
        return 0

    # def solution(numbers, target):
#     cnt1 = recursion(numbers, 0, numbers[0], target)
#     cnt2 = recursion(numbers, 0, -numbers[0], target)
    
#     return cnt1 + cnt2

# def recursion(numbers, idx, result, target):
#     cnt = 0
#     idx += 1
#     if idx == len(numbers):
#         if result == target:
#             cnt += 1
#         return cnt
#     else:
#         cnt1 = recursion(numbers, idx, result + numbers[idx], target)
#         cnt2 = recursion(numbers, idx, result - numbers[idx], target)
#         return cnt1 + cnt2
    
    
