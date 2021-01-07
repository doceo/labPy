## esempio riportato sugli appunti condivisi

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,2,100)

y1 = x**2 + 5*x +10
y2 = 6*x + 3

fig, ax = plt.subplots()
ax.plot(x,y1,color="blue", label="y(x)")
ax.plot(x,y2,color="red", label="y(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.show()