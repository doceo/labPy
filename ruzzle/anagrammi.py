# https://docs.python.org/3/library/itertools.html
from itertools import permutations

'''
Il seguente script genera una lista di anagrammi a partire da una stringa di caratteri data
'''

#generiamo una lista a partire da una stringa
lettere = list("casa")

#generiamo tutte le possibili permutazioni e le inseriamo in una lista
permutazioni = list(permutations(lettere))

#inizializiamo una variabile stringa di appoggio e una lista dove salvarle
temp = ''
anagrammi = []

'''
 il metodo permutations genera una lista di tuple, ognu tupla è una permutazione.
 se scorriamo la lista attraverso un ciclo, possiamo scorrere gli elementi della tupla
 per ricostruire la stringa
'''
for i in permutazioni:
    for carattere in i:
        # in temp concateno tutti gli elementi della tupla così da
        # ottenere i singoli anagrammi della stringa iniziale
        temp += carattere 

    # aggiungo la parola ricostruita dalla tupla alla lista finale degli anagrammi
    anagrammi.append(temp)
    # "svuoto" la variabile temp così da ricostruire un secondo anagramma
    temp = ''

print(anagrammi)
