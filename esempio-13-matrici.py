# una matrice è una lista di liste

# lista 1 | x x x x
# lista 2 | x x x x
# lista 3 | x x x x
# lista 4 | x x x x

# ogni lista è un elemento della lista che chiamiamo tabella

#La seguente tabella possiamo codificarla così:
# A      B      C     D
# 10     11     12    13
# (1,2)  (2,2)  (a,b) Str

riga0 = ['A','B','C','D']
riga1 = [10,11,12,13]
riga2 = [(1,2),(2,2),('a','b'),'Str']

matrice = [riga0,riga1,riga2]
print("matrice è",matrice,"\n")

# individuiamo ogni elemento con doppia parentesi quadra

print("l'elemento matrice[2][1] è",matrice[2][1])
print('che è del tipo ',type(matrice[2][1]),'\n')

## IMPORTANTE ##

# se assegno ad una variabile una lista esistente non faccio
# una copia, ma assegno un riferimento alla variabile originale


materie = ['italiano', 'matematica', 'scienze']

materie_copia = materie

materie[4:4] = ['latino']
print ('materie ',materie)

print (' è stata modificata anche la copia: ',materie_copia, '\n')

# liste nei cicli
i = 0
while i < len(materie):
    print (materie[i],' di lunghezza: ', len(materie[i]))
    i = i +1

