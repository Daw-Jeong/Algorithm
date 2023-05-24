from collections import Counter
def solution(array):
    while len(array) != 0:
        # if len(array) == 1:
        #     return array[0]
        for idx, val in enumerate(set(array)):
            array.remove(val)
        # for entry in enumerate(array):
        #     print(entry)
        if idx == 0: return val
        
    return -1
    
    
    # cnt = Counter(array).most_common()
    # print(cnt)
    # if len(cnt) == 1:
    #     return cnt[0][0]
    # if cnt[0][1] == cnt[1][1]:
    #     return -1
    # return cnt[0][0]
    
    
#     array.sort()
#     count_arr = {}
#     count = 0
    
#     if len(array) == 1:
#         return array[0]
    
#     for i in range(0, len(array)):
#         if i >= 1:
#             if array[i] == array[i-1]:
#                 continue
#         count_arr[array[i]] = array.count(array[i])

#     print(count_arr)

#     max_value = max(count_arr.values())
#     print(max_value)
    
#     for j in count_arr:
#         if count_arr[j] == max_value:
#             count += 1
            
#     if count >= 2:
#         return -1
#     else:
#         for n in count_arr:
#             if count_arr[n] == max_value:
#                 return count_arr[n]