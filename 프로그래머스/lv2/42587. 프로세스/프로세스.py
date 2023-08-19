from collections import deque
def solution(priorities, location):
    answer = 0
    que = deque()
    li = [i for i in range(len(priorities))]
    order = []
    for i in li:
        que.append(i)
    while que:
        temp = que.popleft()
        if priorities[temp] != max(priorities):
            que.append(temp)
        else:
            priorities[temp] = 0
            order.append(temp)
        
    return order.index(location) + 1