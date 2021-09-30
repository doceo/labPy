# La classe retta

class retta:
    def __init__(self,a,b,c):

    # un attributo privato si dichiara con il doppio underscore ( __ )    
        self.__a = a  
        self.__b = b
        self.__c = c

    def equazione(self):
        if(self.__b>0 and self.__c>0):
            return f'{self.__a}x + {self.__b}y + {self.__c} = 0'
        elif(self.__b<0 and self.__c>0):
            return f'{self.__a}x {self.__b}y + {self.__c} = 0'
        elif(self.__b>0 and self.__c<0):
            return f'{self.__a}x + {self.__b}y {self.__c} = 0'
        else:
            return f'{self.__a}x {self.__b}y {self.__c} = 0'


    def trovaY(self, x):
        if self.__b!=0:
            return self.__c/self.__b*x 

    def coppie(self):
        punti = []

        for i in range(1000):
            punti.append((i,self.trovaY(i)))
        return punti


# inizio del programma chiamante


r = retta(-3,-4,-6)

print(r.equazione())
print(r.coppie())

# il metodo dir permette di conoscere tutti i metodi applicabili all'oggetto passato come parametro
print(dir(r))
