n, m = map(int, input().split())
A = [[n*i + j for j in range(m)] for i in range(n)]
print(A)
