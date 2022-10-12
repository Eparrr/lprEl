import numpy as np

a=np.array([i for i in range(1,100)])#1
print(a)

print(a[::3])             #2

b=a[0::3]+a[1::3]+a[2::3]
print(b)                  #3

c=np.reshape(b, (11,3))
print(c)                  #4

d=c.T
print(d)                  #5

e=np.array([i for i in range(-9,2)])
print(np.inner(d,e))      #6

cols =[2,5,8]             #8
r=c[cols , :]
print(r)
print(np.linalg.det(r))






