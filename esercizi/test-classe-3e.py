
# liste
cities = ["Naples", "Milan", "Salerno","Palermo"]
print(cities)
print("il numero di citta' è: " + str(len(cities)))
cities.append("london")
print(cities)
print("il numero di citta' è: " + str(len(cities)))
print(type(cities))
print(type(len(cities)))
print(type(str(len(cities))))

cities.remove("london")
cities.remove(cities[2])
print(cities)

#tuple

fruit = ["apple","banana" ]
tup = (1,4,7,3)
tup = (cities, fruit)
print("stampo tup: ")
print(tup)
print("stampo tipo di tup: " + str(type(tup)))

fruit.append("pera")
print("stampo tup modificato: ")
print(tup)

frase="questa è una frase lunga"
frase_splittata= frase.split()

print(frase_splittata)