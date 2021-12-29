from random import randint

alien = Actor("coin")
coin = Actor("apple_red")


WIDTH = 800
HEIGHT = 800

msg = ""

def draw():
#    coin.pos=(100,100)
#    coin.draw()
    screen.clear()
#    screen.fill("white")
    alien.draw()

def place_alien():
    alien.x = randint(20,WIDTH-20)
    alien.y = randint(20,HEIGHT-20)

def place_coin():
    coin.x = randint(20,WIDTH-20)
    coin.y = randint(20,HEIGHT-20)
    print("coin", coin.pos)

def on_mouse_down(pos):
    if coin.collidepoint(pos):
        print("Bel colpo!!")
        place_alien()
    else:
        print("Mancato!")
        quit()

place_alien()
#place_coin()