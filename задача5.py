S = []
with open('file.txt') as file:
    for line in file:
        S.append(line)
S1 = []
for i in range(1, len(S)):
    S1.append(S[-i].rstrip())
S1.append(S[0].rstrip())
for i in range(0, len(S)):
    for j in range(len(S1[i])):
        print(S1[i][- j - 1], end = '')
    print()
