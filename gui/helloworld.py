# importo dalla libreria le classi di oggetti App e Text
from guizero import App, Text

# creo una istanza di App e la associo all'oggetto app
app = App(title="Hello world")

# creo una istanza dell'oggetto Text e la associo all'oggetto message
message = Text(app, text="Welcome to the Hello world app!")

# restituisco a momitor l'oggetto app
app.display()