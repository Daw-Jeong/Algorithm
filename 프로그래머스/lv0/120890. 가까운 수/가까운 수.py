def solution(array, n):
    array.sort()
    li = [abs(n-i) for i in array]
    return array[li.index(min(li))]
    
    
#     li = [abs(n-i) for i in array]
#     d = min(li)
#     # 가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다. 이거 고려해야해
#     if li.count(d) > 1:
#         temp = [idx for idx in range(len(li)) if li[idx] == d]
#         return min([array[i] for i in temp])
    
#     else:
#         return array[li.index(d)]