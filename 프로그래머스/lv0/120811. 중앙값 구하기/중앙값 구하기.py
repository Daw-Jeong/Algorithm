def solution(array):
    array.sort()
    centerIndex = len(array) // 2
    answer = array[centerIndex]
    return answer