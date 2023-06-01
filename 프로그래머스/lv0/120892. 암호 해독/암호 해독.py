def solution(cipher, code):

    # return ''.join([cipher[i] for i in range(len(cipher)) if (i + 1) % code == 0])
    return cipher[code-1::code]