'''

Open data sui vaccini
https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.csv

il file utilizzato è di esempio, aggiornando dal repository sarà sempre aggiornato

'''
import csv
import datetime
import numpy as np

import matplotlib.pyplot as plt

dataSom = []
primaDose = []
secondaDose = []
docenti = []

# apertura file riga per riga organizzando il risultato in liste
with open('dati-reali-covid/somministrazioni-vaccini-latest.csv', 'r') as file:
    valori = csv.reader(file, delimiter=",")
    header = next(valori)
    for row in valori:
        if((row[17]=="Campania") ):
            dataSom.append(datetime.datetime.strptime(row[0], '%Y-%m-%d')) 
            primaDose.append(int(row[12]))
            secondaDose.append(int(row[13]))
            docenti.append(int(row[11]))

print(header)

print(docenti[2])
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
ax[0].plot(dataSom, primaDose, color="blue", label="uomini")
ax[1].plot(dataSom, secondaDose, color="red", label="donne")
'''
for i in range(2):
    
    ax[i].legend()
'''

# salva il grafico in un file di nome grafico.png
fig.savefig("grafico.png", dpi=100, facecolor="#f1f1f1")
plt.show()