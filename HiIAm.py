# Copyright© by Fin

from tkinter import *

def action():
    name = input("Name: ")
    print("Moin " + name)

fenster = Tk()

button = Button(fenster, text="Drücken", command=action)
button.pack()

mainloop()