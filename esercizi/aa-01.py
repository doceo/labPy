'''
lo script è stato modificato in classe durante la spiegazione, potrebbe 
non essere più coerente
'''

costouno = 45
costodue = 80
costoextra = 40
sosta = int(input("Inserisci numero giorni di sosta "))
azioneuno = "Paga " + str(costouno)
costoextrauno = sosta * costoextra
azioneextradef = "Paga " 
if sosta <= 2:
	print(azioneuno)
elif sosta > 5:
	print("maggiore di..")
else:
	print("paga",costoextrauno)


