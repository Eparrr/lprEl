import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(10,100)
y=np.exp((-x)*(np.sin(x)))
plt.title('График')
plt.grid(which='major',axis='both')
plt.grid(which='minor',axis='both')
plt.xlabel("x")
plt.ylabel("y")
plt.minorticks_on()
plt.plot(x,y)
