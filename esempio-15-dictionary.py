# i dizionari sono collezioni mutabili e non ordinate di coppie chiave-valore
# le chiavi devono essere univoche e non mutabili, quindi non si possono utilizzare le liste, 
# ma stringhe numeri o tuple contenenti oggetti immutabili

# ESEMPI
#                             CHIAVE                 DATO
# Rubrica telefonica        nominativo        Numero di telefono
# elenco insegnanti          materia               nominativo
# cambio valuta          moneta straniera     valore rispetto all'euro


professori = {"matematica": "tripepi", "coding": "mazzone", "disegno":"cori"}
valuta = { "USD": 1.31212, "GBP":0.78244, "CAD":1.45642}

print ("professori: ", professori)
print ("valuta: ",valuta,'\n' )

# accesso agli elementi
prof = professori["matematica"]
print ("accedo all'oggetto relativo alla chiave matematica: ",prof,'\n')

# per aggiungere un elemento devo far riferimento ad una nuova chiave

professori["ed. fisica"]= "crisafo"

print ("professori aggiornato: ", professori,'\n')

# anche nei dizionari possiamo usare la funzione len

print ('il numero di elemnti è len(professori): ',len(professori),'\n')

# anche la verifica dell'esistena nel dizionario si può effettuale come per le altre strutture

# cancellazione di un elemento

del professori['ed. fisica']

print ("professori aggiornato: ", professori,'\n')

# come per le liste, assgnare ad una nuova variabile un dizionario esistente si ottiene
# un riferimento e non una copia del dizionario esistente

# matrici

mat = {(0,0): 'A', (0,1):'B', (0,2):'C', (0,3):'D', (1,0):'E', (1,1):'F', (1,2):'G',(1,3):'H'}


print ("elemento della matrice mat[1,3] è:",mat[1,3],'\n')

