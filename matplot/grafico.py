import matplotlib.pyplot as plt

# per creare un grafico posso affidarmi alla rappresentazione
# di default, inserendo in una tupla i valori dell'asse Y
# l'asse delle X partirà da 0 ed associerà implicamente 
# i valori
plt.plot([4, 3, 2, 1])
plt.show()
print("chiudi il grafico per vedere quello seguente")

# posso anche indicare l'asse X, la prim tupla rappresenterà le X
# la seconda le Y
plt.plot([1, 2, 3, 4],[5,8,2,1])
plt.ylabel('some numbers')
plt.show()

print("chiudi il grafico per vedere quello seguente")

# se vogliamo cambiare il grafico possiamo indicare un terzo parametro.
plt.plot([1, 2, 3, 4],[5,8,2,1],'ro')
# possiamo anche modificare i valori dell'asse X
plt.axis([0, 6, 0, 20])
plt.show()
# per tutti i parametri consulta https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
