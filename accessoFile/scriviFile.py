
# infludiamo questo modulo per creare numeri casuali
from random import randint

# per accedere ad un file devo assegnare
# ad un oggetto il file da aprire, in lettura o scrittura

# associo ad f il file, indico con "w" il tipo di operazione
# così lo aprirà in scrittura (write)

f = open("dati4.txt", 'w')

# definiamo una variabile stringa da riempire con i dati che poi scriverò

# inizializzo la stringa
dati = ""

# il primo ciclo serve a creare le singole righe
for riga in range(100):

    # il secondo ciclo serve a compulare la singola riga
    for elemento in range(1):

        # aggiungo il numero casuale e inserisco uno spazio in coda
        dati = dati + str(randint(1,100)) + "," + str(randint(1,100))
    
    # aggiungo un terminatore di riga, così il secondo rigo va a capo
    dati = dati + "\n"

# avremmmo potuto creare una lista di righe:
# lines = [
#...     'prima riga del file\n',
#...     'seconda riga del file\n',
#...     'terza riga del file\n',
#... ]

print(dati)

# scrivo la stringa nel file
f.write(dati)

# chdiuamo sempre il file
f.close()