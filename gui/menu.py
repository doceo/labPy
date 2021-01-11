# MENU

from guizero import App, MenuBar

def file_function():
    print("File option")

def edit_function():
    print("Edit option")

app = App()
menubar = MenuBar(app,
                  toplevel=["File", "Edit"],
                  options=[
                      [ ["File option 1", file_function], ["File option 2", file_function],["File option 1", file_function], ["File option 2", file_function] ],
                      [ ["Edit option 1", edit_function], ["Edit option 2", edit_function] ]
                  ])
app.display()
