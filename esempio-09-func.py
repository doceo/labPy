#possiamo raggruppare i nostri sottoalgoritmi in funzioni separate
#così da ordinare meglio il codice ed eventualmente riutilizzare le nostre funzioni

#sintassi: 
#def NOMEFUNZIONE (PARAMETRO INPUT)
#   istruzione
#   istruzione
#   istruzione
#   return PARAMETROOUTPUT


import math

def area_del_cerchio (raggio):

# con import possiamo importare un modulo esterno fatto da tante funzioni che possono servirci
# math è il modulo che contiene tutte le funzioni matematiche più complesse delle 4 operazioni
   

# math.pi richiama il valore di pi greco contenuto in path
# math.pow(raggio,2) richiama la funzione potenza, il due eleva al quadrato il primo parametro raggio      
    area=math.pi*math.pow(raggio,2)  

# return restituisce il valore di output alla funzione che l'ha chiamata    
    return area




r1 = float(input("Inserisci il raggio del primo cerchio: "))
r2 = float(input("Inserisci il raggio del secondo cerchio:"))
differenza =abs(area_del_cerchio(r1)-area_del_cerchio(r2))  #abs() restituisce il valore assoluto

print("la differenza tra le due aree è: ", differenza)