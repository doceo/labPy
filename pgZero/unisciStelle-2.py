from random import randint
from time import time

WIDTH = 600
HEIGHT = 600

stelle = []
linee = []

numero_stelle = 8
prossima_stella = 0

tempo_iniziale = 0
tempo_totale = 0
tempo_finale = 0

for stella in range(0,numero_stelle):
    actor = Actor("stella")
    actor.pos = (randint(20, WIDTH -20),randint(20, HEIGHT-70))
    stelle.append(actor)

tempo_iniziale = time()

def draw():
    
    global tempo_totale

    screen.blit("cielo",(0,0))    
    num = 1

    for stella in stelle:
        screen.draw.text(str(num),(stella.pos[0]-3,stella.pos[1] +14))
        stella.draw()
        num = num + 1

    for linea in linee:
        screen.draw.line(linea[0], linea[1],(255,255,255))

    if prossima_stella < numero_stelle:
        tempo_totale = time() - tempo_iniziale
        # screen.draw.text(str(tempo_totale), (10, 10) ,fontsize=30)
        screen.draw.text(str(round(tempo_totale, 2)), (10, 10) ,fontsize=30)
    else:
        # screen.draw.text(str(tempo_totale), (10, 10) ,fontsize=30)
        screen.draw.text(str(round(tempo_totale, 2)), (10, 10) ,fontsize=30)

def on_mouse_down(pos):

    global prossima_stella
    global linee

    if prossima_stella < numero_stelle:
        if stelle[prossima_stella].collidepoint(pos):
            if prossima_stella:
                linee.append((stelle[prossima_stella-1].pos, stelle[prossima_stella].pos))
            prossima_stella = prossima_stella + 1
        
        else:
            linee = []
            prossima_stella = 0
