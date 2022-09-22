with open('file.txt', encoding='utf-8') as file:
    res = []
    for line in file:
        line = line.strip().split()
        res.append(line)
    res.sort(key=lambda x: x[0])
    for i in res:
        print(i[0], i[1], i[3])
