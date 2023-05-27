# n = int(input())
# for i in range(1,n+1):
#     print("*"*i)

print('\n'.join('*' * (i + 1) for i in range(int(input()))))
