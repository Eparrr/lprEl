gen={i for i in range(25)}
print(gen)
def ok(in_num):
    if (in_num%3)!=0:
        return True
    else:
        return False
print(list(filter(ok,gen)))

