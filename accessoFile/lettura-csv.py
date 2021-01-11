import csv
# apertura file riga per riga organizzando il risultato in liste
with open('testcsv.csv', 'r') as file:
   reader = csv.reader(file)
   for row in reader:
       print(row)

print("")
print("")

# apertura del file riga per riga organizzando l'output come dictionary
with open("testcsv.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))