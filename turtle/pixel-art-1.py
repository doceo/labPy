import turtle

schermo = turtle.Screen()
schermo.setup(width=400, height=300)
schermo.title("Pixel Art")
turtle_pixel = turtle.Turtle()
turtle_pixel.speed(1) # Velocità massima disegno

def disegna_pixel(x, y, colore, pixel_size):
    turtle_pixel.penup()
    turtle_pixel.goto(x, y) # Posiziona in alto-sinistra del pixel
    turtle_pixel.pendown()
    turtle_pixel.fillcolor(colore)
    turtle_pixel.begin_fill()
    for _ in range(4): # Disegna un quadrato
        turtle_pixel.forward(pixel_size)
        turtle_pixel.right(90)
    turtle_pixel.end_fill()

# Colori (nome o RGB esadecimale)
rosso = "red"

# Disegna un pixel rosso alla posizione (50, 50) (turtle usa coordinate centrali, quindi aggiustiamo)
disegna_pixel(50 - 10, 50 + 10, rosso, 20) # Approssimando per centrare

schermo.mainloop() # Mantieni la finestra aperta