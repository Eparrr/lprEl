S = input().split()
a = []
for i in range(3):
    a.append(set(S[i]))
a[0] &= a[1]
a[0] &= a[2]
print(a[0])
