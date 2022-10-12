import numpy as np
a=np.array([1,2])
b=np.array([3,4])
print(np.matmul(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)))
