def solution(num, total):
    # start = (total - num * (num - 1) // 2) // num
    # return [i for i in range(start, start + num)]
    
    return [(total - num * (num - 1) // 2) // num + i for i in range(num)]