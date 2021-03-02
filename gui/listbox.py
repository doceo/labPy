""""
GUIZERO - listbox
"""
from guizero import *


def f1():
    output.append("Questo è il primo tasto")

def f2():
    for i in range(0,5):
        output.append(i)
        i+=1

def f3():
    output.append("FINE")

def selectf():
    output.append(lista.value)

app = App(title="Esempio ", width=500, height=600, bg="#e3adad")

p1 = PushButton(app,text='bottone 1',command=f1)
p2 = PushButton(app,text='bottone 2',command=f2)
p3 = PushButton(app,text='bottone 3',command=f3)

menubar = MenuBar(app,
                  toplevel=["File", "Edit"],
                  options=[
                      [ ["File option 1", f1], ["File option 2", f1],["File option 3", f1], ["File option 4", f1]  ],
                      [ ["Edit option 1", f1], ["Edit option 2", f1] ]
                  ])

lista = ListBox(app, items=["Matematica", "Italiano", "Scienze", "Latino"], selected="Matematica", command=selectf, grid=None,
                align="center",
                visible=True,
                enabled=True,
                multiselect=False,
                scrollbar=True,
                width=200,
                height=100)

output = TextBox(app, width=80, height=10, multiline=True)

p1.bg = "#c0e3ad"
p2.bg = "#c0e3ad"
p3.bg = "#c0e3ad"
output.bg = "#c5ade3"

app.display()

