import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10 , 10 , 100)
y1 = x
y2 = x**2
y3 = x**3
plt.plot(x,y1)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = x")
plt.grid()
plt.show()
plt.plot(x,y2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = x^2")
plt.grid()
plt.show()
plt.plot(x,y3)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = x^3")
plt.grid()
plt.show()


