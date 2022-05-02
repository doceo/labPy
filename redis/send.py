import redis

# Module for warm-up
from time import sleep

from random import randint

# connect with redis server

r = redis.Redis(host='10.255.237.221', port=6379, password='1357642rVi0', db=0)


print(r)
# Loop is the variable needed to save
loop = 0

# Run loop for three hours
while (loop<10):

    msg = "Ho fatto " + str(randint(10, 100)) + ' punti!'
    r.publish('game_123', msg )
    print('\n',msg)
    loop += 1
    sleep(3)