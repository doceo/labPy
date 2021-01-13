from guizero import *

def Moltiplica(a, b):
    x = int(a.value)
    y = int(b.value)

    risultato = x * y
    output.value = risultato

app = App(title="Moltiplica",bg="#f5f5f5")

output = TextBox(app, width=80, height=10, multiline=True)

etichettaA = Text(app, text="Inserisci A:")
paramB = TextBox(app)
etichettaB = Text(app, text="Inserisci B:")
paramB = TextBox(app)

pushB = PushButton(app, text="Moltiplica!", command=Moltiplica, args=[paramB, paramB])
app.display()

