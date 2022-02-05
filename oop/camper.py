'''
importo la classe auto, così da rendere la sua implementazione
disponibile all'interprete
'''

from auto import auto

class camper(auto):

    def __init__(self, proprietario, marca, modello, cilidrata, cavalli, colore, allestimento):

        # rimanda al costruttore della classe padre che si occupa degli attributi ereditati
        super().__init__(proprietario, marca, modello, cilidrata, cavalli, colore)
        self.__allestimento = allestimento


    def scheda(self):
        scheda = f'''\n allestimento:{self.__allestimento}'''
        # utilizza il metodo "scheda()" ereditato 
        return super().scheda() + scheda

# INIZIO DEL PROGRAMMA CHIAMANTE

if __name__ == "__main__":

    pippo = camper("pippo","Ford","Transit",2500, 1600, "giallo","laika")

    marco = auto("marco","fiat","Bravo",2500, 200, "verde")

    print(pippo.scheda())
    print(marco.scheda())
  