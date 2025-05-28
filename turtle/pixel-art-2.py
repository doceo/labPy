import turtle

# Impostazioni iniziali
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pixel Art con Turtle")

pixel_size = 20  # Dimensione di ogni pixel
grid_size = 10   # Numero di pixel per lato (10x10)

# Funzione per disegnare un quadrato (pixel)
def draw_pixel(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(4):
        turtle.forward(pixel_size)
        turtle.left(90)
    turtle.end_fill()

# Funzione per disegnare la griglia
def draw_grid():
    start_x = -pixel_size * grid_size // 2
    start_y = pixel_size * grid_size // 2

    for i in range(grid_size):
        for j in range(grid_size):
            x = start_x + j * pixel_size
            y = start_y - i * pixel_size
            draw_pixel(x, y, "white")  # Colore di base bianco

# Definizione della pixel art (10x10)
pixel_art = [
    ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black"],
    ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
    ["black", "white", "black", "black", "black", "black", "black", "black", "white", "black"],
    ["black", "white", "black", "white", "white", "white", "white", "black", "white", "black"],
    ["black", "white", "black", "white", "black", "black", "white", "black", "white", "black"],
    ["black", "white", "black", "white", "white", "white", "white", "black", "white", "black"],
    ["black", "white", "black", "black", "black", "black", "black", "black", "white", "black"],
    ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
    ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black"],
    ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
]

# Funzione per disegnare la pixel art
def draw_pixel_art():
    start_x = -pixel_size * grid_size // 2
    start_y = pixel_size * grid_size // 2

    for i in range(grid_size):
        for j in range(grid_size):
            x = start_x + j * pixel_size
            y = start_y - i * pixel_size
            draw_pixel(x, y, pixel_art[i][j])

# Esecuzione
turtle.speed(0)
turtle.hideturtle()
draw_grid()
draw_pixel_art()

turtle.done()