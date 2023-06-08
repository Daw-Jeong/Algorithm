def solution(dots):
    answer = 0
    if incline(dots[0], dots[1]) == incline(dots[2], dots[3]):
        return 1
    if incline(dots[0], dots[2]) == incline(dots[1], dots[3]):
        return 1
    if incline(dots[0], dots[3]) == incline(dots[1], dots[2]):
        return 1
    return answer

def incline(li1, li2):
    return (li1[1] - li2[1]) / (li1[0] - li2[0])