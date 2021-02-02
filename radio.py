from tkinter import *
from PIL import ImageTk, ImageTk
root = Tk()

#r = IntVar() #definimos la variable del radio button dependiendo el tipo de dato que le estamos pasando
#r.set("2")

MODES= [
    ('queso','queso'),
    ('cebolla','cebolla'),
    ('tuco','tuco'),
    ('rucula','rucula')
]

pizza = StringVar()
pizza.set("queso")
#loop para crear radio buttons a partir de una lista
for text, mode in MODES:
    Radiobutton(root,text= text,variable= pizza, value = mode).pack()

def clicked(value):
    label = Label(root, text = value)
    label.pack()


#Radiobutton(root,text="Option 1", variable = r, value = 1,command= lambda : clicked(r.get())).pack()
#Radiobutton(root,text="Option 2", variable = r, value = 2,command= lambda : clicked(r.get())).pack()
#le damos cualquier nombre a la variable

label = Label(root, text = pizza.get())
label.pack()
btn = Button(root,text="click", command=lambda : clicked(pizza.get()))
btn.pack()
mainloop()