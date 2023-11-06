def solution(brown, yellow):
    answer = []
    x = 3
    while True:
        y = brown/2 + 2 - x
        if x * y == brown + yellow:         
            return [y, x]
        else:
            x += 1

# x + y = brown/2 + 2
# (x-2) * (y-2) = yellow
# x * y = brown + yellow
# x >= y