def solution(s):
    if s[0].isalpha():
        s = s[0].upper() + s[1:]
    for i in range(1, len(s)):
        if s[i-1] == ' ' and s[i].isalpha():
            s = s[:i] + s[i].upper() + s[i+1:]
        else:
            s = s[:i] + s[i].lower() + s[i+1:]
    return s
        