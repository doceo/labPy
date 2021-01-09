import csv
 
with open('testcsv.csv', 'r') as file:
   reader = csv.reader(file)
   for row in reader:
       print(row)

print("")
print("")

with open("testcsv.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))