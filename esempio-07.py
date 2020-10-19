#strutture iterative
#somma tra due numeri

N = int(input("inserisci N: "))
i=1

somma = 0

while i <= N:
    somma = somma + i
    i = i + 1

print ("la somma dei primi",str(N),"numeri è", str(somma) )
