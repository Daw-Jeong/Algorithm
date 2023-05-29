def solution(array, height):
    
    # return len([i for i in array if i > height])
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)