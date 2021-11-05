# La classe retta

class retta:
    def __init__(self, tipo = "param", p1 = None, p2 = None, p3 = None, p4 = None):
        if(tipo=="param"):
            # un attributo privato si dichiara con il doppio underscore ( __ )    
            self.__a = p1  
            self.__b = p2
            self.__c = p3
            self.__punti = []
            self.__m = m()

        elif(tipo == "punti"):
            # inserire la procedura per ricavare a, b, c a partire da due punti.
            pass
               
        elif(tipo == "coeff"):
            # inserire la procedura per ricavare a, b, e c a partire dal coefficiente angolare ed un punto. 
            pass
 
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c

    def eqEsplicita(self):
        '''
        restituire in output la forma implicita della retta
        '''
        return 0

    def eqImplicita(self):
        '''
        restituire in output la forma implicita della retta
        '''
        return 0

    def trovaY(self, x):
        '''
        restituire in output la forma esplciita della retta
        '''
        return 0

    def punti(self, N, M):
        '''
        definire il metodo che a partire da N ed M genera tutte le coppie (tuple) di x e y 
        appartengono alla retta nell'intervallo N e M dell'asse X.
        '''

    def m(self):
        '''
        restituire il coefficiente angolare a valle delle dovute verifiche
        '''
        return 0

    def intersezione(self, s):
        '''
        acquisita una retta s in input, questo metodo deve restituire il punto in comune 
        (sottoforma di tupla), verificandone l'esistenza. Restituire "null" se le rette sono 
        in parallelo oppure la lista __punti() se le rette dovessero coincidere. 
        '''
        return 0

