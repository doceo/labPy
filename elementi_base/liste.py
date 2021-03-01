# le liste sono molto simili alle tuple e tutte le operazioni 
# applicate alle tuple possono essere applicate alle liste

# le liste sono MUTABILI (le tuple no)

# la lista è una sequenza ordinata e mutabile di valori non 
# necessariamente dello stesso tipo

# DIFFERENZA TRA LISTA E TUPLA
elencoUno = [4,7,2,3]
elencoDue = (4,7,2,3)


print("elencoUno è una ", type(elencoUno))
print("elencoDue è una ", type(elencoDue))

lista = elencoUno

print ("\nl'elemento 1 di lista è ", lista[1]  )

print("\nLa sua lunghezza è ", len(lista))

lista = lista + ['paolo', 'giovanni', 'mario']

print ("\nla lista adesso è:")

# stampa tramite ciclo di for
for elemento in lista:
    print(elemento)

# stampa di una lista intera
print(lista)
# oppure stamparne solo una porzione
print("\nalcune porzioni:")
print(lista[4:])
print(lista[:4])

print ("\nLa lista è diventata di", len(lista), "elementi")

'''
è possibile annidare liste, signifca che un suo elemento può 
essere una lista. Poichè sono oggetti mutabili è possibile manipolarle 
aggiungendo altri elementi (con le tuple non è possibile)
'''

lista[3] = ['pane', 'pasta', 3, 6,1]

print('\n','visualizziamo la lista annidata','\n',lista)

print('\nPosso eliminare elementi in due modi.\n')
lista[0:1] = []
print("lista[0:2], la lista diventa:",lista,'\n')

del lista[2]
print ("del lista[2], la lista diventa:", lista,'\n')

listarange = range(10)
listarange2 = range(2,10,2)

# stampa di liste generate con range

print("listanrange")
for elemento in listarange:
    print(elemento)
print("listarange2")
for elemento in listarange2:
    print(elemento)


# verifica della presenza di un elemento.

print(7 in listarange)
print(7 in listarange2, "\n")
