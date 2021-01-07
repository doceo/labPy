a = int(input("Inserisci valore a: "))
b = int(input("Inserisci valore b: "))
c = int(input("Inserisci valore c: "))
print(str(a) + str("x^2"), "+", str(b) + str("x"), "+", str(c), "= 0")
if b != 0:  
    if c != 0:
        delta = int(int(int(b**2)) - int(4) * int(a) * int(c))
        print(str("delta = "), str(delta))
        if delta != 0:
            x1 = str(((int(-1) * int(b)) + int(delta)) / (int(2) * int(a)))
            x2 = str(((int(-1) * int(b)) - int(delta)) / (int(2) * int(a)))
            print("x1 = ", str(x1))
            print("x2 = ", str(x2))
            print("L'equazione è completa")
        else:
            x1 = str((int(-1) * int(b)) / (int(2) * int(a)))
            x2 = x1
            print("x1 = ", int(x1))
            print("x2 = ", int(x2))
            print("L'equazione è completa")
    else:
        x1 = int(0)
        x2 = int(int(-1) * int(b) / int(a))
        print("x1 = ", str(x1))
        print("x2 = ", str(x2))
        print("L'equazione è spuria")
else:
    if c != 0:
        x1 = int(-1) * (int(((int(-1) * int(c)) / int(a)) **(1/2)))
        x2 = int(((int(-1) * int(c)) / int(a)) **(1/2))
        print("x1 = ", str(x1))
        print("x2 = ", str(x2))
        print("L'equazione è spuria")
    else:
        x1 = int(0)
        x2 = int(x1)
        print("x1 = ", str(x1))
        print("x2 = ", str(x2))
        print("L'equazione è monomia")