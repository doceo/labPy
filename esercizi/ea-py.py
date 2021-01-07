stringa = input("qual è la parola di cui vuoi sapere le lettere? = ")
stringa1 = list(stringa)
print(stringa1)
alphabet = ('abcdefghijklmnopqrstuwxyz')
alphabet1 = list(alphabet)

lista = []
for alphabet1 in stringa1:
    if stringa1.count(alphabet1) > 0:
        lista.append((alphabet1, stringa1.count(alphabet1)))

int(lista)
copia_lista = stringa1
m = set(copia_lista)
print(m, max(lista))