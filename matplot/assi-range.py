
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

# definisco le x della curva
x = np.linspace(0,30,500)

# definisco le y della curva
y = np.sin(x) * np.exp(-x/10)

fig, axes = plt.subplots(1,3,figsize=(9,3), subplot_kw={'facecolor':"#ebf5ff"})

axes[0].plot(x,y,lw=2)
axes[0].set_xlim(-5,35)
axes[0].set_ylim(-1,1)
axes[0].set_title(" valori definiti")

axes[1].plot(x,y,lw=2)
axes[1].axis('tight')
axes[1].set_title("axis('tight')")

axes[2].plot(x,y,lw=2)
axes[2].axis('equal')
axes[2].set_title("axis('equal')")

plt.show()
