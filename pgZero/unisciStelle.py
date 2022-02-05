from random import randint

WIDTH = 600
HEIGHT = 600

stelle = []
linee = []

prossima_stella = 0

for stella in range(0,8):
    actor = Actor("stella")
    actor.pos = (randint(20, WIDTH -20),randint(20, HEIGHT-70))
    stelle.append(actor)

def draw():
    screen.blit("cielo",(0,0))
    num = 1
    for stella in stelle:
        screen.draw.text(str(num),(stella.pos[0]-3,stella.pos[1] +14))
        stella.draw()
        num = num + 1

    for linea in linee:
        screen.draw.line(linea[0], linea[1],(255,255,255))


def on_mouse_down(pos):

    global prossima_stella
    global linee

    if stelle[prossima_stella].collidepoint(pos):
        if prossima_stella:
            linee.append((stelle[prossima_stella-1].pos, stelle[prossima_stella].pos))
        prossima_stella = prossima_stella + 1
    
    else:
        linee = []
        prossima_stella = 0
