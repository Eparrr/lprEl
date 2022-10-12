import numpy as np
a=np.array([(1,2),(1,1)])
b=np.array([(3,4),(2,2)])
c=np.array([(0,0),(3,3)])
print(a)
print(b)
print(np.matmul(a,b))
print(np.matmul(a,c))
