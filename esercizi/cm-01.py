a = int(input ("inserisci il valore del modulo del termine di secondo grado: "))
b = int(input ("inserisci il valore del modulo del termine di primo grado: "))
c = int(input ("inserisci il valore del modulo del termine noto: "))
d = (b**2)+(-4*a*c)

if a==0:
    print ("l'equazione è di primo grado")
    
if b==0:
    print ("l'equazione è pura")
    w=(-c/a)**(1/2)
    x1 = -w
    x2 = +w
    print (x1)
    print (x2)

if c==0:
    print ("l'equazione è spuria")
    x1= 0
    x2= -b/a
    print (x1)
    print (x2)

if a!=0 and b!=0 and c!=0 :
    print ("l'equazione è completa")
    if d>0:
        print("ci sono due soluzioni")
        x1 = (-b+d**(1/2))/(2*a)
        x2 = (-b-d**(1/2))/(2*a)
        print(x1)
        print (x2)

    if d==0:
         print("c'è una soluzione")
         x= -b/(2*a)
         print (x)

    if d<0:
       print("non ci sono soluzioni")
          
