
import csv
import matplotlib.pyplot as plt
import numpy as np


# apertura file riga per riga organizzando il risultato in liste
dati = []
tempo = []
asseX = []
asseY = [] 
asseZ = []

with open("accessoFile/RawData.csv", 'r') as file:
   reader = csv.reader(file)
   for row in reader:
       dati.append(row)
       tempo.append(row[0])
       asseX.append(row[1])
       asseY.append(row[2])
       asseZ.append(row[3])
       #print(row)

print(tempo)
tempo.pop(0)
asseX.pop(0)
asseY.pop(0)
asseZ.pop(0)
print(tempo)


#fig, ax = plt.subplots(1, 3, figsize=(14,3))




left, bottom, width, height = 0.1, 0.1, 0.8, 0.8  

fig, ax = plt.subplots(1, 1)

ax.plot(tempo,asseX,color="blue", label="y1")
#ax[1].plot(tempo,asseY,color="red", label="y2")
#ax[2].plot(tempo,asseZ,color="green", label="y3")

'''
for i in range(3):
    ax[i].set_xlabel("x")
    ax[i].set_ylabel("y")
    ax[i].legend()

'''
plt.show()
