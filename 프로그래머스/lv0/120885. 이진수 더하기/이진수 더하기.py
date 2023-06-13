def solution(bin1, bin2):
    sumbi = str(int(bin1) + int(bin2))

    for i in range(1, len(sumbi)):
        if int(sumbi[len(sumbi) - i]) >= 2:
            sumbi = sumbi[:len(sumbi) - i - 1] + str(int(sumbi[len(sumbi) - i - 1]) + 1) + str(int(sumbi[len(sumbi) - i]) % 2) + sumbi[len(sumbi) - i + 1:]
    
    if int(sumbi[0]) >= 2:
        sumbi = '1' + str(int(sumbi[0]) % 2) + sumbi[1:]
        
    return sumbi