a = []
with open('file.txt', encoding='utf-8') as file:
    for line in file:
        s = line.split()
        a.append(s[-2:])
    print(a)
    a = sorted(a, key = lambda x: x[1], reverse = True)
    print(a)
    i = 1
    print(a[0][1])
    k = 1
    while a[k][1] == a[k - 1][1]:
        print(a[k][0], end = ' ')
        k += 1
