# gli insiemi sono collezioni mutabili non ordinate di valori distinti
# quindi non è possibile riferirsi ad una posizione per trovare un elemento

luoghi = {'napoli', 'roma', 'milano', 'roma', 'venezia', 'napoli'}

# se stampiamo eliminerà i doppioni e l'ordine non sarà rispettato
print (luoghi, '\n')
print(type(luoghi))

# possiamo realizzare tutte le operazioni tra insiemi
#   Unione                  A | B
#   Intersezione            A & B
#   Differenza              A - B
#   Differenza Simmetrica   A ^ B

luoghi_noti = {'milano', 'napoli', 'caserta', 'avellino'}

print ('luoghi | luoghi_noti ', luoghi | luoghi_noti, ' \n' )
print ('luoghi & luoghi_noti ', luoghi & luoghi_noti, ' \n' )
print ('luoghi - luoghi_noti ', luoghi - luoghi_noti, ' \n' )
print ('luoghi ^ luoghi_noti ', luoghi ^ luoghi_noti, ' \n' )

# SET 
# il comando permette di trasfromare una stringa, lista o tupla in un insieme
# così da poter elimanare doppioni, si può trasformare anche in direzione inversa

nome = 'raffaella'
lettere = set(nome)
print (lettere, '\n')

# conversione per eliminare doppioni

lista_luogni = ["napoli", "napoli", "roma", "milano", "caserta"]

# copia di un insieme

stessi_luoghi = lista_luogni

# tutte le operazioni fatte sull'insieme di partenza le ritroviamo
# nell'insieme copia
print (stessi_luoghi)

# se faccio operazioni tra insiemi invece creo oggetti nuovi

luoghi_noti = luoghi_noti | {'palermo'}

print (luoghi_noti,'\n')

# è possibile scorrere un insieme anche con i cicli

for luogo in luoghi:
    print(luogo, 'di lunghezza ',len(luogo))



