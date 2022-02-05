'''
PRINT
'''
a = 124523

print(a, file=sys.stdout)

# posso descrivere il valore da stampare, separando con la virgola

print("a= ",a)

parola1 = "casa"
parola2 = "albero"
parola3 = "montagna"

print(parola1, parola2, parola3, sep="--")

a = range(1,10)

for i in a:
    print(i, end='')

for j in a:
    print(j)