import numpy as np
import random
a=np.array([random.randint(0,64) for i in range(8) for j in range(8)])
b=np.reshape(a,(8,8))
print(b)
i,j=map(int,input().split())
q=b[i]
r=b[:][j]
print(q)
print(r)
z=np.hstack([q,r])
x=np.reshape(z,(4,4))
print(x)
print("Минор ",np.linalg.det(x))
