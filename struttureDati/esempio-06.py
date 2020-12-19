#questo programma saluta l'utente nella lingua scelta

nome = input("nome= ")
lingua = input("Nazionalità: ")

if lingua == "ITA":
    saluto = "ciao"

elif lingua == "FRA":
    saluto = "Salut"

elif lingua == "NDL":
    saluto = "Hoi"

elif ((lingua == "GBR") or (lingua == "USA")):
    saluto = "hello"

else:
    saluto = "?"

print(saluto,",",nome)