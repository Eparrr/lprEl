import numpy as np
a=np.array([(1,2),(2,2)])
b=a.T
print(a)
print(b)
print(np.linalg.det(a))   # определитель матрицы
print(np.linalg.det(b))   # определител транспонированной матрицы

a[1]=0*a[1]
print(a)
print(np.linalg.det(a)) #определитель матрицы с нулевой строкой

a=np.array([(1,2),(2,2)])
b=np.array([a[1],a[0]])
print(b)
print(np.linalg.det(b)) #опр. "зеркальной" матрицы

a=np.array([(1,2),(1,2)])
print(a)
print(np.linalg.det(a))  #с одинаковыми строками

a=np.array([(1,2),(2,2)])
print(a)
a[0]=2*a[0]
print(np.linalg.det(a)) #определитель матрицы с первой строкой,умноженной на 2

a=np.array([(1,2),(2,2)])
a[0]=a[0]+2*a[1]
print(a)
print(np.linalg.det(a)) #1я строка+2я*2,определитель




