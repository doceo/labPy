#seleziona il più grande tra i tre numeri

a = float(input("inserisci a: "))
b = float(input("inserisci b: "))
c = float(input("inserisci c: "))

if a>b:
    if a>c:
        max = a
    else:
        max = c
else:
    if b>c:
        max = b
    else:
        max = c

print ("tra ", a,",",b, " e ",c," il maggiore è ",max)