def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if (n - i * (i - 1) / 2) > 0 and (n - i * (i - 1) / 2) % i == 0:
            answer += 1
    return answer

# i*x + i*(i-1)/2 = n
# i*(i+1)/2  