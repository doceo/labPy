'''
Salvare su file una struttura dati complessa
e successivamente ricaricarla dal file

dettagli sul modulo JSON sono reperibili alla pagina descrittiva
https://docs.python.org/3/library/json.html

'''
import json

dati = {

    "uno" : [1],
    "due" : {"uno": "a", "due": "b"},
    "tre" : [(1,),(4,3),(2,6,8)],
    "quattro": "una stringa",
    "cinque" : {"uno": 1, "due": 2, "tre":3, "quattro": 4}

}

''' 
salvare su file su file
parametri di input per dump:
json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, 
allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

'''
with open("data.json", "w") as f:
    json.dump(dati, f, indent=4)

f.close()

# estrapolo da file

with open("data.json", "r") as f:
    dati_da_file = json.load(f)

f.close()

print("stampa il file intero: ",dati_da_file)

# oppure un singolo elemento
print("stampa il valore associato alla chiave tre':",dati_da_file["tre"])

