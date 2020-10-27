#introduzione alle tuple
#Una tupla è una sequenza ordinata e immutabile di valori non necessariamente
#dello stesso tipo e si racchiudono tra parentesi tonde

tupla = (7, 4, 16, 34)
parole = ( 'foglia', 'casa', 'pompieri', 'albero' )

print ('tupla: ', tupla, '\n') #\n aggiunge una riga sotto alla parola mandata in output

print ('parole: ',parole, '\n')

#un elemento di una tupla può essere a sua volta una tupla
elementi = (1, 'ancoraparole', 4,'enumeri', ('tuple', 'di', 'tuple' ))

print ('elementi: ', elementi, '\n')

#posso concatenare le tuple
print('concateno due tuple: ',tupla + parole, '\n')

#accedo agli elementi di una tupla tramite le parentesi quadre []
print('parole[0]:',parole[0], '\n')

#il tipo di rsultato dipende dal tipo di dato inserito nella tupla.
#la funzione type() restituisce il tipo di valore che bisogna analizzare
print('parole[0] è',parole[0],'ed è di tipo:')
print(type(parole[1]), '\n')
print('invece elementi[0] (', elementi[0],') è di tipo')
print (type(elementi[0]), '\n')

#lunghezza di una tupla
print('la lunghezza della tupla PAROLE è:', len(parole), '\n')

#è possibile estrarre solo una sotosezione della tupla con NOME[inizio:fine]

print ('elementi[1:4]:',elementi[1:4],'\n')

#è possibile verificare l'appartenenza di una tupla:
print('verifichiamo se 7 è presente nella tupla PAROLE.')
print('la sintassi usa la parola chiave IN, quindi: ')
print('"7 in parole" restituisce',7 in parole,'\n')
print("'foglia' in parole, invece restituisce", 'foglia' in parole,'\n' )

#posso anche confrontare due tuple
amici1 = ('mario', 'paolo', ' francesco')
amici2 = ('MARIO', 'paolo', 'francesco')
print('amici1 < amici2: ',amici1 < amici2)
print('invece amici1 > amici2: ',amici1 > amici2)
print("perchè le lettere minuscole seguono quelle maiuscole nell'ordinamento",'\n')

#possiamo inoltre stampare attraverso un ciclo tutta la tupla
for elemento in elementi:
    print(elemento, " è di tipo", type(elemento))
