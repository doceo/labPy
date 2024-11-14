'''

Open data sui vaccini
https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.csv

il file utilizzato è di esempio, aggiornando dal repository sarà sempre aggiornato

'''
import csv
import datetime
import numpy as np

import matplotlib.pyplot as plt
tempo = []
asseX = []
asseY = []
asseZ = []
modulo = []

# apertura file riga per riga organizzando il risultato in liste
with open('dati-3.csv', 'r') as file:
    valori = csv.reader(file, delimiter=",")
    header = next(valori)
    for row in valori:
        t = row[0].replace(',', '.')
        tempo.append(float(t))
        x = row[1].replace(',', '.')
        asseX.append(float(x))
        y = row[2].replace(',', '.')
        asseY.append(float(y))
        z = row[3].replace(',', '.')
        asseZ.append(float(z))
        m = row[4].replace(',', '.')
        modulo.append(float(m))

print(header)
print(asseX)
file.close()

fig, ax = plt.subplots(1, 2, figsize=(14,3))
#fig, ax = plt.subplots()

# generiamo una matrice di una riga per 4 colonne da inserire in Figure
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8 

# x = np.linspace(-5,5,100)
'''
# generiamo le quattro istanze Axes, inserendo i valori dei 4 grafici
ax[0].plot(dataSom,donne,color="blue", label="donne")
ax[1].plot(dataSom,uomini,color="red", label="uomini")
'''
ax[0].plot(tempo, asseX, color="blue", label="asseX")
ax[1].plot(tempo, asseY, color="red", label="asseY")
'''
for i in range(2):
    
    ax[i].legend()
'''

# salva il grafico in un file di nome grafico.png
fig.savefig("grafico.png", dpi=100, facecolor="#f1f1f1")
plt.show()