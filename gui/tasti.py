
#GUIZERO

from guizero import *
from random import *

def tasto1():
    output.append("abbiamo un testo")
    output.append("fine del primo output")  
    output.append("")

def tasto2():
    for i in range(0,5):
        output.append(i)
        i+=1
    output.append("fine del secondo output")
    output.append("")

def tasto3():
    output.append(randint(0,100))
    output.append("fine del terzo output")
    output.append("")

app = App(title="Esempio", width=500, height=300, bg="#f4d742")

output = TextBox(app, width=80, height=10, multiline=True)

p1 = PushButton(app,text='bottone 1',command=tasto1)
p2 = PushButton(app,text='bottone 2',command=tasto2)
p3 = PushButton(app,text='bottone 3',command=tasto3)

p1.bg = "#41f465"
p2.bg = "#41f465"
p3.bg = "#41bbf4"
output.bg = "#ccc222"

app.display()

