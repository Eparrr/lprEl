d = {(i - 96): chr(i) for i in range(97, 123)}
dstroke = {value: key for key, value in d.items()}
s = set(input())
print(s)
res = 0
for i in s:
    res += dstroke[i]
print(res)
