S = input().split()
a = []
i=0
while i<len(S):
    a.append(set(S[i]))
    i+=1
i=0
while i<len(S):
    a[0] &= a[i]
    i+=1
print(a[0])
