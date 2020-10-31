# in questo file ci sono alcune funnzioni base
# sulle stringhe

# UNA STRINGA È UNA SEQUENZA ORDINATA DI CARATTERI


# concatenazione

nome = "paolo"
spazio = ' '
cognome = 'esposito'

frase = nome + spazio + cognome

print(frase)
print()
# possiamo usare apici '' o virgolette ""

# se abbiamo bisogno di usare apici, rachciudiamo
# la stringa tra virgolette e viceversa.

apice = "usiamo l'apostrofo"
virgolette = 'o "virgolettare" un testo'

print (apice)
print (virgolette)
print()
# accesso agli elementi di una stringa

print('la quarta lettera di virgolette è: ',virgolette[4] )
print()
# una stringa è immutabile, non possiamo cambiare
# un singolo carattere la l'intera stringa si

# virgolette[4] = r restituirebbe errore

virgolette = "cambio la stringa" #posso farlo

print(virgolette)
print()
# lunghezza di una stringa
n = len(virgolette)
print ("virgolette contiene", n, "caratteri")
print()

# Sezioni di stringa, posso estrarre una parte della stringa
print("estrapoliamo porzioni dalla variabile 'virgolette'")
s = virgolette[3:6]
print (s)
print(virgolette[5:8])

print('primi 4 caratteri: ',virgolette[:4])
print('dal quarto alla fine: ',virgolette[4:])
print()

#appartenenza ad una stringa verifica 
#l'esistenza di uno o più caratteri e restituisce
# TRUE o FALSE

print('frase: ', frase)
print('verifichiamo se "a" è presente: ', 'a' in frase)
print('verifichiamo se "paolo" è presente: ', 'paolo' in frase)
print('verifichiamo se "paola" è presente: ', 'paola' in frase)
print()

#confronto tra stringhe
# == uguaglianze
# < e > precedenza alfabetica

nome1 = 'mario'
nome2 = 'MARIO'

print("verifichiamo se 'nome1' è uguale a 'nome2'", nome1==nome2)
print("verifichiamo se 'nome1' è > di 'nome2'", nome1>nome2)
print()

# ESEMPI CON CICLI
# la funzione len() restituisce il numero di caratteri
# la funzione ord() restituisce il codice numerico associato al carattere

print (frase)
i=0

print("ciclo while")
while i < len(frase):
    print(frase[i], " ", ord(frase[i]))
    i = i + 1

print("ciclo for")
for lettera in frase:
    print(lettera, " ", ord(lettera))