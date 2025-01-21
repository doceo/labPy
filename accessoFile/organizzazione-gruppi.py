import csv

prenotazioni=[]

with open('gruppi.csv', 'r') as file:
    reader = csv.reader(file,delimiter=',')
    for row in reader:
            #print(row)
            prenotazioni.append(row[5])
#    header = next(reader)

#print("Le colonne sono: ",header)
print("le righe del file sono: ")
print(prenotazioni)

lista_giorni=[]

giorni_str =""

for str in prenotazioni:
    if ";" in str:
        giorni_str = str.split(";")
        prenotazioni.remove(str)
        for g_split in giorni_str:
            lista_giorni.append(g_split)

print(lista_giorni)

giorni_dic = {}

for gg in lista_giorni:
    if gg not in giorni_dic:
        occ = lista_giorni.count(gg) 
        giorni_dic[gg] =occ
    
print(giorni_dic)
print("")



