import turtle

tarty = turtle.Turtle()
tarty.speed('slow')

for i in range(36):
 for j in range(6):
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


'''
tarty.circle(100, 180)
tarty.left(90)
tarty.penup()

tarty.goto(-100,100)
'''

wait = input("premi invio per chiudere.") 
