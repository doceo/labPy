import turtle

tarty = turtle.Turtle()
tarty.speed('fast')

for n in range(36):
    for i in range(6):
        tarty.forward(100)
        tarty.left(60)
    tarty.right(10)


'''
si sarebbe potuto racchiudere l'esagono in una funzione.

def esagono():
    for i in range(6):
        tarty.forward(100)
        tarty.left(60)

for i in range(36):
    esagono()
    tarty.right(10)

'''


wait = input("premi invio per chiudere.") 
