weight = 50
planet = int(input("write a number from 1 to 9"))

if planet == 1:
    weight = 0.378*weight
elif planet == 2:
    weight = 0.907*weight
elif planet == 3:
    weight = 1*weight
elif planet == 4:
    weight = 0.377*weight
elif planet == 5:
    weight = 2.36*weight
elif planet == 6:
    weight = 0.916*weight
elif planet == 7:
    weight = 0.889*weight
elif planet == 8:
    weight = 1.12*weight
else:
    weight = 0.071*weight

print(weight)