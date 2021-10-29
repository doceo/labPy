'''
word -> deve contenere la stringa da analizzare
carattere -> è il dictionary all'interno del quale salvare le informazioni 
count -> contiene il numero totale di ripetizioni
nCaratteri -> contiene il numero di caratteri che si ripetono
'''

word = list("giraffa")  # in ruzzle conterrà l'attributo di istanza che contiene la lista di caratteri

carattere = {}

nCaratteri = 0
count = 0

for i in word:

    if (i in carattere):  # se trova il carattere nel dictionari incrementa il suo valore
        carattere[str(i)] += 1
    else:
        carattere[str(i)] = 1 # se non lo trova lo aggiunge

for i in carattere:
    if carattere[i]>1: # se trova una lettera ripetuta
        count+=1 # incrementa il numero di caratteri che si ripetono
        nCaratteri += carattere[i] # incrementa il numero totale di ripetizioni

print(count)
print(nCaratteri)