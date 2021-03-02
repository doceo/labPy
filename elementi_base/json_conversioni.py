
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
print("convertiamo un dizionario", z)

# oggetto lista: 
y = [ "name", "John", "age", 30, "city", "New York"]

# conversione in JSON:
z = json.dumps(x)

# risultato:
print("convertiamo una lista", z)