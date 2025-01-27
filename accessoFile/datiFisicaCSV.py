
import csv

name = input("indica il nome del file: ")

path ="accessoFile/"
namePath =  path + name
# apertura file riga per riga organizzando il risultato in liste
with open(namePath, 'r') as file:
   reader = csv.reader(file)
   for row in reader:
       print(row)

print("")
print("")
