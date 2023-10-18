#bfs? target의 인덱스까지의 최단거리?
def solution(begin, target, words):
    if target not in words:
        return 0
    
    words.insert(0, begin)
    words.remove(target)
    words.append(target)
    
    n = len(words)
    li = [[] for _ in range(n)]
    print(words)
    
    for i in range(n):
        for l in range(n):
            li[i].append(changable(words[i], words[l]))
    
    
    for k in range(n):
        for i in range(n):
            for l in range(n):
                li[i][l] = min(li[i][l], li[i][k] + li[k][l])
        
    print(li)
    
    return li[0][n - 1]

def changable(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    if cnt > 1:
        return 1e9
    elif cnt == 0:
        return 0
    else:
        return 1