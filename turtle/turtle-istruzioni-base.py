'''
per tutte le istruzioni relative al modulo turtle si faccia riferimento alla documentazione
della libreria
https://docs.python.org/3/library/turtle.html
'''


from turtle import Turtle, Screen

# inizializzo la tartaruga
tarty = Turtle()

# per visualizzare una tartaruga al posto della freccia
tarty.shape('turtle')

# visualizza uno sfondo e assegna un colore con la codifica RGB esadecimale
sfondo = Screen()
sfondo.colormode(255)

R = 0
G = 255
B = 0
sfondo.bgcolor((R, G, B))

# per identificare la posizione della tartaruga

print(tarty.xcor(), tarty.ycor())

'''
movimenti della tartaruga
La velocità può essere inpostata d un valore compreso tra 1 o 10.
Esistono anche velocità standard
‘fastest’ :  0
‘fast’    :  10
‘normal’  :  6
‘slow’    :  3
‘slowest’ :  1
'''

tarty.speed('normal')

tarty.pensize(10) # definisce lo spessore della penna
tarty.reset() # cancella lo schermo
tarty.forward(100) # va avanti di 100 pixel
tarty.right(90) # gira a destra
tarty.backward(90) # cammina all'indietro indietro di 90 pixel
tarty.left(90) # gira a sinistra
tarty.color('red') # definisce un colore
tarty.circle(20) # genera un cerchio con il raggio di 10 pixel
tarty.penup() # "alza la penna" dal foglio, quindi non scrive
tarty.forward(100)
tarty.pendown() # abbassa la penna sul foglio per scrivere
tarty.goto(100,-200) # salta alla posizione
#tarty.setpos(100,100) uguale a goto()
#tarty.setposition(100,100) uguale a goto()
tarty.hideturtle() # nasconde la tartaruga
tarty.forward(100)
tarty.showturtle()

aspetta = input("clicca un tasto")