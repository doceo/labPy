import matplotlib.pyplot as plt
import csv
# Apriamo il file .csv
with open("dati.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")

    # Inizializziamo le liste per i dati
    x = []
    y1 = []
    y2 = []
    y3 = []

    # Leggiamo i dati dal file
    for row in reader:
        y1.append(float(row[1]))
        y2.append(float(row[2]))
        y3.append(float(row[3]))

    # Creiamo i grafici
    plt.scatter(y1)
    plt.title("Grafico 1")
    plt.xlabel("Numero di riga")
    plt.ylabel("Colonna 2")


    # Mostriamo i grafici
    plt.show()