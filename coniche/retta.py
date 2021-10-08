# La classe retta

class retta:
    def __init__(self,a,b,c):

    # un attributo privato si dichiara con il doppio underscore ( __ )    
        self.__a = a  
        self.__b = b
        self.__c = c
        self.__punti = []
    
    def __init__(self, p1, p2):
        '''
        questo costruttore deve generare una retta a partire da due punti.
        p1 e p2 sono tuple che identificano le coordinate dei punti a partire
        dai quali vanno ricavati a,b e c ed inizializzati gli attributi di istanza
        '''

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

