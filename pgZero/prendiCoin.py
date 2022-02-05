from random import randint

WIDTH = 800
HEIGHT = 800

score = 0

game_over = False

coin = Actor("coin")
coin.pos = 200,200

cat = Actor("gatto1")
cat.pos = 100,200


def time_up():
    global game_over
    game_over = True


def draw():

    screen.clear()
    screen.fill("blue")
    coin.draw()
    cat.draw()

    screen.draw.text("Score: " + str(score), color="white", topleft=(10,10), fontsize = 40)

    if game_over:
        screen.fill("pink")
        screen.draw.text("Punteggio finale: " + str(score), topleft=(10,10), fontsize = 60)



def place_coin():
    coin.x = randint(20, (WIDTH-20))
    coin.y = randint(20, (HEIGHT-20))

def update():

    global score

    coin_collected = cat.colliderect(coin)

    if coin_collected:
        score = score + 10
        place_coin()


    if keyboard.left:
        cat.x = cat.x - 2
    elif keyboard.right:
        cat.x = cat.x + 2
    elif keyboard.up:
        cat.y = cat.y - 2
    elif keyboard.down:
        cat.y = cat.y + 2

clock.schedule(time_up,10.0)

place_coin()
