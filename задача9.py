a = [0, 0, 0]
counts = [0, 0, 0]
with open('file.txt', encoding='utf-8') as file:
    for line in file:
        s = line.split()
        print(s)
        ball = int(s[3])
        clas = int(s[2])
        a[clas - 9] += ball
        counts[clas - 9] += 1
for i in range(3):
    print(a[i]/counts[i], end = ' ')
