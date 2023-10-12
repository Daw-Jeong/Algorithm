def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])

# def solution(numbers, target):
#     answer = recursion(numbers, -1, 0, target)
#     return answer

# def recursion(numbers, idx, result, target):
#     idx += 1
    
#     if idx < len(numbers):
#         cnt1 = recursion(numbers, idx, result + numbers[idx], target)
#         cnt2 = recursion(numbers, idx, result - numbers[idx], target)
#         return cnt1 + cnt2
        
#     else:
#         if result == target:
#             return 1
#         return 0
