from turtle import Turtle, Screen

tarty = Turtle()
sfondo = Screen()

sfondo.colormode(255)

R = 0
G = 255
B = 0
sfondo.bgcolor((R, G, B))

tarty.speed(1)
tarty.turtlesize(10)

# quadrato
tarty.goto(-100,-100)

tarty.begin_fill() # inizia un disegno a colore pieno   
tarty.color('red')
for i in range(4):
    tarty.forward(100)
    tarty.left(90)
tarty.end_fill() # finisce il disegno a colore pieno

tarty.penup()
tarty.goto(100,-100)
tarty.pendown()
tarty.begin_fill() # inizia un disegno a colore pieno
tarty.color('blue')


for i in range(5):
    tarty.forward(100)
    tarty.left(60)

tarty.end_fill() # finisce il disegno a colore pieno

wait = input("Premi invio per continuare") 