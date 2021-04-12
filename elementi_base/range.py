'''
RANGE
'''

# UN PARAMETRO: sottinde iniziare da 0
sequenza = range(10)
print("\n\n prima sequenza: ")
for i in sequenza:
    print(i, end=' ')

sequenza2 = range(5,10)


# DUE PARAMETRI: inizio e fine
print("\n\n seconda sequenza: ")
for j in sequenza2:
    print(j, end=' ')

# TRE PARAMETRI: inizio, fine e step
print("\n\n terza sequenza: ")
sequenza3 = range(5,20,2)
for k in sequenza3:
    print(k, end=' ')

print("\n")