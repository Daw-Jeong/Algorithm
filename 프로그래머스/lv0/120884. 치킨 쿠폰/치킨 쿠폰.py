def solution(chicken):
    count = 0

    while chicken >= 10:
        count += chicken // 10
        leftover = chicken % 10
        chicken = chicken // 10 + leftover
        
    return count