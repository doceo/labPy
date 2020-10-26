costouno = 45
costodue = 80
costoextra = 40
sosta = int(input("Inserisci numero giorni di sosta "))
azioneuno = "Paga " + str(costouno)
costoextrauno = sosta * costoextra
azioneextradef = "Paga " 
if sosta < 2:
	print(azioneuno)
else:
	print("paga",costoextrauno)