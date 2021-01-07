## esempio riportato sugli appunti condivisi

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,2.5), facecolor="#f5f5f5")  # i colori vanno passati come stringa, 
                                                        # il colore è ricavato dalla codifica esadecimale RGB

# la posizione di Axes la determiniamo come distanza dai bordi
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8  
ax = fig.add_axes((left, bottom, width, height), facecolor="#e1e1e1")

x = np.linspace(-5,5,100)

y1 = x**2 + 5*x +10
y2 = 6*x**2 + 3
y3 = x**5 + 6*x**2 + 4*x+2

ax.plot(x,y1,color="blue", label="y1")
ax.plot(x,y2,color="red", label="y2")
ax.plot(x,y3,color="green", label="y3")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

# salva il grafico in un file di nome grafico.png
fig.savefig("grafico.png", dpi=100, facecolor="#f1f1f1")
plt.show()