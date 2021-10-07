# classe calcolo combinatorio

class combinazioni():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self):
        #modificare questo metodo in modo da verificare la coerenza delle variabili di
        #istanza presenti
        return 0

    def combPos(self,k):

        return self.__N**k

    def combUtil(self):
        '''
        verificare se la STRINGA attributo di istanza è presente
        nel file word.italian.txt 
        '''
        return 0


