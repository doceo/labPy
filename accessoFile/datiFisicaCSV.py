
import csv

name = input("indica il nome del file: ")

path ="accessoFile/"
namePath =  path + name
# apertura file riga per riga organizzando il risultato in liste
dati = []
tempo = []
asseX = []
asseY = [] 
asseZ = []

with open(namePath, 'r') as file:
   reader = csv.reader(file)
   for row in reader:
       dati.append(row)
       tempo.append(row[0])
       asseX.append(row[1])
       asseY.append(row[2])
       asseZ.append(row[3])
       #print(row)

print("vettore tempo ")
print(tempo)
print("vettore asseX ")
print(asseX)
print("vettore asseY ")
print(asseY)
print("vettore asseZ ")
print(asseZ)

print("")


for i in asseX:
    if int(i)>2:
        print