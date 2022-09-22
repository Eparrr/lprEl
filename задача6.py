a = [0, 0, 0]
with open('file.txt', encoding='utf-8') as file:
    for line in file:
        s = line.split()
        print(s)
        ball = int(s[3])
        clas = int(s[2])
        if ball > a[clas - 9]:
            a[clas - 9] = ball
print(*a)
