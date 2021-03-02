import numpy as np
import matplotlib.pyplot as plt
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10,4))
fig.suptitle('Example of a Single Legend Shared Across Multiple Subplots')

# valori
x =  [1, 2, 3]
y1 = [1, 2, 3]
y2 = [3, 1, 3]
y3 = [1, 3, 1]
y4 = [2, 2, 3]

# etichette delle linee
line_labels = ["prima linea", "seconda linea", "terza linea", "quarta linea"]

# creo le istanze dei grafici
l1 = ax1.plot(x, y1, color="red")[0]
l2 = ax2.plot(x, y2, color="green")[0]
l3 = ax3.plot(x, y3, color="blue")[0]
l4 = ax3.plot(x, y4, color="orange")[0] # A second line in the third subplot

# Creo la legenda
fig.legend([l1, l2, l3, l4],     # associo i grafici
           labels=line_labels,   # associo le etichette
           loc="center right",   # posiziono la legenda
           borderaxespad=0.1,    # la distanzio dai bordi
           title="etichette delle linee"  # assegno un titolo
           )

# posiziono la legenda all'interno dell'area di lavoro
plt.subplots_adjust(right=0.85)

plt.show()