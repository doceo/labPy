
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)

plt.annotate("curva quadratica",xy=(1.2,0),fontsize=12, family="serif", rotation = 30)

plt.plot(t, t**2)

plt.show()
