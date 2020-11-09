
porte = dict() #definiamo un dizionario

for i in range(1,101):porte[i]= 'C'     # chiudo tutte le porte

for p in range(1,101):                  # ciclo su tutte le porte
    for i in range(p,101):              # ciclo che inizia dalla porta p
        if i%p == 0:
            if porte[i] == 'C':         # se è chiusa la apro
                porte[i] = 'A'
            else:
                porte[i]= 'C'

print("sono aperte le porte ")
for i in porte:
    if porte[i] == 'A':
        print(i)
        