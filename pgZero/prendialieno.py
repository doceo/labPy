from random import randint

alien = Actor("alien")

def draw():
    screen.clear()
    alien.draw()

def place_alien():
    alien.x = randint(10,800)
    alien.y = randint(10,600)


def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Bel colpo!!")
        place_alien()
    else:
        print("Mancato!")
        quit()

place_alien()
