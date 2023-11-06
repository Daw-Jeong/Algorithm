def solution(nums):
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    if len(nums)//2 >= len(dic):
        return len(dic)
    else:
        return len(nums)//2
