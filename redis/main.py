# https://redis.io/commands/

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

# inizializzo la lista delle chiavi del DB
r.keys()

# r.set('chiave, "valore')

r.set('mario', 'lasuaPassword')
value = r.get('mario') 
print(value)

# valore incrementale

r.incr('count')
print(r.get('count'), " e incremento...")

r.incr('count')
print(r.get('count'))

print("\nControlliamo ora le chiavi: ",r.keys())

for i in range(10):
    r.rpush("lista", str(i))

print("\nestraiamo dalla lista: ")
print(r.rpush("lista", 3))

print("\noppure estraiamo la sua lunghezza ed un range: ")
print(r.llen("lista")," elementi, tra il 2 ed 8: ", r.lrange("lista", 2,8))
