import csv
# inizializzo un vettore dentro cui salvare la tabella
popolazione = []

'''
apertura file riga per riga organizzando il risultato in liste
salvate in POPOLAZIONE, il risultato finale sarà una matrice

'''

with open('Foglio1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        popolazione.append(row)

# elimino la prima riga, per elaborare la colonna della
# popolazione
popolazione.pop(0)

popolazioneTot = 0.; # da notare il punto dopo lo 0 ad indicare che
                     # la variabile conterrà un valore reale

print("somma della popolazione residente:")
for popol in popolazione:
    popol[3] = popol[3].replace(".","") # elimino i punti 
    popol[3] = popol[3].replace(",",".")# covnerto la virgola in punto

    popolazioneTot = popolazioneTot + float(popol[3]) # converto in numero reale


print("la popolazione totale è: ",popolazioneTot)
