import csv
import matplotlib.pyplot as plt

# Leggi il file csv
with open("dati.csv", "r") as f:
    reader = csv.reader(f)
    data = list(reader)

# Crea le liste dei valori x e y per ciascuna colonna
t_values = [float(row[0]) for row in data]
x_values = [float(row[1]) for row in data]
y_values = [float(row[2]) for row in data]
z_values = [float(row[3]) for row in data]

# Crea i grafici
plt.figure()
plt.scatter(t_values, y_values, label="acc. X")
plt.title("accellerazione X")
plt.legend()
plt.savefig("grafico_x.png")
plt.close()

plt.figure()
plt.scatter(t_values, y_values, label="acc. y")
plt.title("accellerazione y")
plt.legend()
plt.savefig("grafico_y.png")
plt.close()

plt.figure()
plt.scatter(t_values, z_values, label="acc. z")
plt.title("accellerazione z")
plt.legend()
plt.savefig("grafico_z.png")
plt.close()

