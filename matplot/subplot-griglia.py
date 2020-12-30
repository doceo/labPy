## esempio riportato sugli appunti condivisi

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 4, figsize=(14,3))

# generiamo una matrice di una riga per 4 colonne
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8  
 
x = np.linspace(-5,5,100)

y1 = x**2 + 5*x +10
y2 = 6*x**2 + 3
y3 = x**5 + 6*x**2 + 4*x+2
y4 = np.cos(20*x)


ax[0].plot(x,y1,color="blue", label="y1")
ax[1].plot(x,y2,color="red", label="y2")
ax[2].plot(x,y3,color="green", label="y3")
ax[3].plot(x,y4,color="yellow", label="y4")

for i in range(3):
    ax[i].set_xlabel("x")
    ax[i].set_ylabel("y")
    ax[i].legend()

# salva il grafico in un file di nome grafico.png
fig.savefig("grafico.png", dpi=100, facecolor="#f1f1f1")
plt.show()