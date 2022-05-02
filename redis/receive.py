from config import *

from time import sleep
import redis


# connect with redis server as Bob
r = redis.Redis(host='10.255.237.221', port=6379, password='1357642rVi0', db=0)

mario = r.pubsub()

# subscribe to classical music
mario.subscribe('game_123')

# Loop is the variable needed to save
loop = 0

# Run loop for three hours
while (loop<20):
    # ignore Bob subscribed message
    try:
        print(mario.get_message()['data'])
    except:
        pass
    
    sleep(3)
    loop += 1