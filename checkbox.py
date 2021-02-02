from tkinter import *
from PIL import ImageTk, Image

root = Tk()

def show():
    label = Label(root,text=var.get()).pack()


#variable de tkinter
var = StringVar()

c = Checkbutton(root,text = "checkbox", variable = var,onvalue="on", offvalue="off")
c.deselect()
c.pack()


btn = Button(root,text = "mostrar", command = show).pack()
root.mainloop()