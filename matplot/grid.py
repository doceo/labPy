
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

# definisco le x della curva
x = np.linspace(0,30,500)

# definisco le y della curva
y = np.sin(x) * np.exp(-x/10)

fig, axes = plt.subplots(1,3,figsize=(9,3))

# definisco quali ticks devo evidenziare come minor e come major e li salvo nelle relative variabili
x_major_ticker = mpl.ticker.MultipleLocator(4)
x_minor_ticker = mpl.ticker.MultipleLocator(1)
y_major_ticker = mpl.ticker.MultipleLocator(0.5)
y_minor_ticker = mpl.ticker.MultipleLocator(.25)

axes[0].plot(x,y,lw=2)
axes[0].set_xlim(-5,35)
axes[0].set_ylim(-1,1)
axes[0].set_title(" valori definiti")

#associo al grafico i minor e major ticker
axes[0].xaxis.set_major_locator(x_major_ticker)
axes[0].xaxis.set_minor_locator(x_minor_ticker)
axes[0].yaxis.set_major_locator(y_major_ticker)
axes[0].yaxis.set_minor_locator(y_minor_ticker)

# definisco una griglia per il primo grafico, che identifica i major ticks
axes[0].grid(color="grey", which="major", linestyle='-', linewidth=0.5)

axes[1].plot(x,y,lw=2)
axes[1].axis('tight')
axes[1].set_title("axis('tight')")

#associo al grafico i minor e major ticker
axes[1].xaxis.set_major_locator(x_major_ticker)
axes[1].xaxis.set_minor_locator(x_minor_ticker)
axes[1].yaxis.set_major_locator(y_major_ticker)
axes[1].yaxis.set_minor_locator(y_minor_ticker)

# definisco una griglia per il secondo grafico, che identifica i minor ticks
axes[1].grid(color="grey", which="minor", linestyle=':', linewidth=0.25)

axes[2].plot(x,y,lw=2)
axes[2].axis('tight')
axes[2].set_title("axis('tight')")

#associo al grafico i minor e major ticker
axes[2].xaxis.set_major_locator(x_major_ticker)
axes[2].xaxis.set_minor_locator(x_minor_ticker)
axes[2].yaxis.set_major_locator(y_major_ticker)
axes[2].yaxis.set_minor_locator(y_minor_ticker)

# definisco una griglia per il terzo grafico, che identifica i major ticks sull'asse y
# e i minor ticks sull'asse x
axes[2].grid(color="grey", which="minor", axis='y', linestyle=':', linewidth=0.5)
axes[2].grid(color="grey", which="major", axis='y', linestyle='-', linewidth=0.5)
axes[2].grid(color="grey", which="minor", axis='x', linestyle=':', linewidth=0.5)


plt.show()
