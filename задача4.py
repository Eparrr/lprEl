f = open('file.txt')
S = f.readlines()
for i in range(len(S)):
    print(S[len(S) - i - 1][:-1])
f.close
