animals = ["dog","cat","tiger","turtle"]
fruits = [3,5,6,7,7]

print(animals)

print("la lunghezza della lista è: " + str(len(animals)))
animals.append("cow")
print(animals)

print("la lunghezza della lista è: " + str(len(animals)))

animals.append(4)

print(animals)

animals.append(fruits)

print(animals[6][1])

animals[6].append("cow")
print(animals)

print(animals[6])

animals[0]+=" cow"
animals[6][0]+=5
print(animals)

fruits.append(100)

print(animals)
print(fruits[3]+fruits[4])
