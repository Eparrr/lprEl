import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(50,100)
y=x*(np.sin(x))**2
plt.title('График')
plt.grid(which='major',axis='both')
plt.grid(which='minor',axis='both')
plt.xlabel("x")
plt.ylabel("y")
plt.minorticks_on()
plt.plot(x,y)
