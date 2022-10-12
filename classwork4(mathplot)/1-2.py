import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,100,10)
y=(x**(-2))*np.sin(x)
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(x,y)
