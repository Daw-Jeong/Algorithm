def solution(spell, dic):

    for ch in spell:
        dic = [s for s in dic if ch in s]

    return 1 if len(dic) != 0 else 2