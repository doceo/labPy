
'''
STRUTTURA DI UN OGGETTO JSON
[
    { 
    "nome":"Edoardo",   
    "cognome":"Rossi",
    "matricola":"S13663",
    "corsi_precedenti":2,   
    "laureato":true  
    },
    { 
    "nome":"Paolo",   
    "cognome":"Bianchi",
    "matricola":"S643577",
    "corsi_precedenti":3,   
    "laureato":true  
    },
    { 
    "nome":"Renato",   
    "cognome":"Gialli",
    "matricola":"S753578",
    "corsi_precedenti":4,   
    "laureato":false
    }

]

'''

import json

# oggetto dictionary:
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}


# conversione in JSON:
z = json.dumps(x)

# risultato:
print("convertiamo un dizionario", z, "\n")

# oggetto lista: 
y = [ "name", "John", "age", 30, "city", "New York"]

# conversione in JSON:
z = json.dumps(y)

# risultato:
print("convertiamo una lista", z, "\n")

# conversione in JSON, ma con indentazione:
z = json.dumps(x, indent=4)

# risultato:
print("convertiamo una lista, ma con l'indentazione", z)

dic = json.loads(z)

print("z: ",type(z))
print("dic: ",type(dic),"\n")

print("alcune conversioni da oggetto Python a stringa di tipo JSON")
print("True ",json.dumps(True))
print("False ",json.dumps(False))
print("None ",json.dumps(None))
print("lista ",json.dumps(["apple", "banana"]), " in vettore")
print("Tupla ",json.dumps(("apple", "banana")), " in vettore")