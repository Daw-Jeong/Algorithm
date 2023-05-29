def solution(rsp):

    for i in range(len(rsp)):
        if rsp[i] == '2':
            rsp = rsp[0:i] + '0' + rsp[i+1:]
        elif rsp[i] == '0':
            rsp = rsp[0:i] + '5' + rsp[i+1:]
        else:
            rsp = rsp[0:i] + '2' + rsp[i+1:]

    return rsp