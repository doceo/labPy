
stringa = input("Scrivere una stringa ")
lista_lettere = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("i numeri di volte in cui le lettere si ripetono all'interno della stringa è")
stringa = list(stringa.upper())
for lettera in lista_lettere:
    if stringa.count(lettera) > 0:
      print(lettera, " = ",stringa.count(lettera))