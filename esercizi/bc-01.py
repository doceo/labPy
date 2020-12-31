#equazione di secondo grado.py

a=int(input("inserisci il valore di a"))
b=int(input("inserisci il valore di b"))
c=int(input("inserisci il valore di c"))
 
if a!=0 & b!=0 & c!=0:
 print("l'equazione è completa")
 delta=int(b^2-4*a*c)
 x1=int(-b**2*delta/2*a) #elevazione a potenza con ** ma devi indicare l'indice della potenza
 x2=int(-b**2*delta/2*a)
 
if b==0:
 print("l'equazione è pura")
 x1=int(-b**2-c/a)  #cosa hai elevato a potenza?
 x2=int(+b**2-c/a)

if c==0:
 print("l'equazione è spuria")
 x1=int(0)
 x2=int(-b/a)
 


