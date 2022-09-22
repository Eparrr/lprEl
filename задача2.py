n, m = map(int, input().split())
A = [[2*(j < i) + (i < j) for j in range(m)] for i in range(n)]
print(A)
