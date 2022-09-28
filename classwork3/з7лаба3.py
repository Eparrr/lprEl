n = int(input())
d = dict()
for i in range(n):
    s = input().split()
    d[s[0]] = s[1]
s = input()
if s in d:
    print(d[s])
else:
    print()
