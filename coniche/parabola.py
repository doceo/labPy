'''
PARABOLA
La classe parabola deve gestire un oggetto relativo alla rappresentazione e costruzione
di una parabola.

- Il costruttore dovrà tenere conto di tutte le possibilità di generazione di una parabola.
-- tramite parametri (a,b,c)
-- tramite fuoco e direttrice
-- rapporti con altri ogggetti (tangenza con rette, passaggio per punti ecc..)

'''

class parabola:
    def __init__(self, tipo = "param", p1 = None, p2 = None, p3 = None, p4 = None):
        if(tipo=="param"):
            # un attributo privato si dichiara con il doppio underscore ( __ )    
            self.__a = p1  
            self.__b = p2
            self.__c = p3
            self.__punti = []

        elif(tipo == "fuocoDiret"):
            # inserire la procedura per ricavare a, b, c a partire l fuoco e della direttrice.
            pass
        
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c

    def fuoco(self):
        pass

    def direttrice(self):
        pass
    