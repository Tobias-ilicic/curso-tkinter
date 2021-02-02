from tkinter import *
from PIL import ImageTk, Image

root = Tk()

clicked = StringVar()
clicked.set("Lunes")

options = ["Lunes",
"Martes",
"Miercoles",
"jueves"
]

drop = OptionMenu(root,clicked,*options)
drop.pack()


root.mainloop()