def solution(lines):
#     answer = 0
#     li = []
#     for el in lines:
#         for i in range(el[0], el[1]):
#             li.append(i)
            
#     for l in range(min(lines)[0], max(lines[0][1], lines[1][1], lines[2][1])):      
#         if li.count(l) >= 2:
#             answer += 1

#     return answer

    sets = [set(range(start, end)) for start, end in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])


    