import string
import numpy as np
import matplotlib.pyplot as plt


def estraiDati(nomeFile):

    # apriamo il file in lettura
    f = open(nomeFile, 'r')

    # usiamo il metodo readlines 
    # per ottenere una lista di righe del file

    # stampiamo la prima riga
    # print(f.readline()) 

    # possiamo fare un ciclo e prendere riga per riga 

    coordX = []
    coordY = []

    # da notare che posso fare un ciclo all'interno di un file
    # direttamente sulle righe

    for riga in f:
        valori = str(f.readline())  # converto in stringa la riga
        valori = valori.strip('\n') # elimino i lterminatore di riga
        valori = valori.split(',')  # separo la stringa in due numeri
        valori = list(valori)       # converto in lista
        print(valori)
        coordX.append(int(valori[0])) # aggiungo la coordinata X
        coordY.append(int(valori[1])) # aggiungo la coordinata Y

    f.close()  # chiudiamo il file

    coordX.sort()

    print ("X: ",coordX)
    print ("Y: ",coordY)

    # ottengo a partire dalle coordinate un array di tipo numpy
    # ordinando l'asse delle X
    p = np.array([coordX,coordY]) 

    # ordino l'arrei rispetto alle valori della X, prima coordinata 

    print("p= ", p)

    # stampo il tipo di dato di p, per verificare sia di tipo ndarray
    print(type(p))

    # restituisco il vettore bidimensionale p
    return p


graf1 = estraiDati("dati1.txt")

graf2 = estraiDati("dati2.txt")

graf3 = estraiDati("dati3.txt")

graf4 = estraiDati("dati4.txt")

fig, ax = plt.subplots(1, 4, figsize=(14,3))

# generiamo una matrice di una riga per 4 colonne da inserire in Figure
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8 

x = np.linspace(-5,5,100)

# generiamo le quattro istanze Axes, inserendo i valori dei 4 grafici
ax[0].plot(graf1[0],graf1[1],color="blue", label="y1")
ax[1].plot(graf2[0],graf2[1],color="red", label="y2")
ax[2].plot(graf3[0],graf3[1],color="green", label="y3")
ax[3].plot(graf4[0],graf4[1],color="yellow", label="y4")

for i in range(3):
    ax[i].set_xlabel("x")
    ax[i].set_ylabel("y")
    ax[i].legend()


# salva il grafico in un file di nome grafico.png
fig.savefig("grafico.png", dpi=100, facecolor="#f1f1f1")
plt.show()