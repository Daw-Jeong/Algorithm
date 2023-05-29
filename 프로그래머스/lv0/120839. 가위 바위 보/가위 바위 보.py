def solution(rsp):
    rsp = rsp.replace('2', 's')
    rsp = rsp.replace('0', 'r')
    rsp = rsp.replace('5', 'p')
    rsp = rsp.replace('s', '0')
    rsp = rsp.replace('r', '5')
    rsp = rsp.replace('p', '2')
    return rsp

    # dic = {'2':'0','0':'5', '5':'2'}
    # return ''.join([dic[rsp[i]] for i in range(len(rsp))])

#     for i in range(len(rsp)):
#         if rsp[i] == '2':
#             rsp = rsp[0:i] + '0' + rsp[i+1:]
#         elif rsp[i] == '0':
#             rsp = rsp[0:i] + '5' + rsp[i+1:]
#         else:
#             rsp = rsp[0:i] + '2' + rsp[i+1:]

#     return rsp