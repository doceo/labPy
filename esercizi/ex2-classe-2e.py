#liste e cicli di for
#una lista è un insieme ordinato di elementi e si rappresentano 
# chiuse tra parentesi quadre separati da virgole

settimana = ['LUN', 'MAR', 'MER', 'GIO', 'VEN', 'SAB', 'DOM']

#posso stampare un elmenento in particolare
print ("primo giorno: ",settimana[4])

#se voglio stampare tutta la lista posso usare un ciclo di for che ha la seguente sintassi
#for VARIABILE in LISTA:
#    istruzione_1
#    istruzione_2
#    ...
#    ...
#istruzione successiva al ciclo
print("la settimana è: ")
for x in settimana:
    print(x)

print()


#attraverso range posso generare numeri che vanno da un min ad un max: range(min,max)
#range(start, stop, step)    stop non è incluso

print("range(3,9,2): ")

# [3,4,5,6,7,8,9]
#range (3,10,2)
#range(6)

intervallo = range(3,9,2)
for x in intervallo:
    print(x)

print()


print("range(11): ")

primi_n = range(11)
for x in primi_n:
    print(x)

print()

print("range(0,30,2):" )
pari_minori_di_30 = range(0,30,2)  
for x in pari_minori_di_30:
    print(x)
#len() restituisce il numero degli elementi della lista
print("sono", len(pari_minori_di_30), "elementi")

