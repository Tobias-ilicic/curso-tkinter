from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("400x400")

def slide(var):
    root.geometry(str(horizontal.get()) + "x" + str(VERTICAL.get()))

VERTICAL = Scale(root,from_=0, to=200, command = slide)
VERTICAL.pack()


horizontal = Scale(root,from_=0, to=200, orient=HORIZONTAL,command=slide)
horizontal.pack()

#Podemos obtener el numero en el que esta el slider con el get

boton= Button(root,text="te doy el numero", command=slide).pack()
root.mainloop()