from random import randint

alien = Actor("alien")

WIDTH = 800
HEIGHT = 800

msg = ""

def draw():
    screen.clear()
    screen.fill("red")
    alien.draw()
    screen.draw.text(msg,topleft=(WIDTH/2-30,10), color="white" , fontsize=32)


def place_alien():
    alien.x = randint(10,WIDTH-10)
    alien.y = randint(10,HEIGHT-10)

def on_mouse_down(pos):
    global msg
    if alien.collidepoint(pos):
        msg ="Bel colpo!!"
        print(msg)
        
        place_alien()
    else:
        msg ="mancato!"
        print(msg)
        quit()

place_alien()
