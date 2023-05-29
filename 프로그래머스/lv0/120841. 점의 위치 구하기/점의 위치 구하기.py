def solution(dot):
    result = [[3, 2], [4, 1]]
    return result[dot[0] > 0][dot[1] > 0]

    # if dot[0] > 0:
    #     if dot[1] > 0:
    #         return 1
    #     else:
    #         return 4
    # else:
    #     if dot[1] > 0:
    #         return 2
    #     else:
    #         return 3
