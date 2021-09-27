# La classe retta

class retta:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def equazione(self):
        if(self.b>0 and self.c>0):
            return f'{self.a}x + {self.b}y + {self.c} = 0'
        elif(self.b<0 and self.c>0):
            return f'{self.a}x {self.b}y + {self.c} = 0'
        elif(self.b>0 and self.c<0):
            return f'{self.a}x + {self.b}y {self.c} = 0'
        else:
            return f'{self.a}x {self.b}y {self.c} = 0'


    def trovaY(self, x):
        if self.b!=0:
            return self.c/self.b*x 

    def coppie(self):
        punti = []

        for i in range(1000):
            punti.append((i,self.trovaY(i)))
        return punti

r = retta(-3,-4,-6)

print(r.equazione())
print(r.coppie())