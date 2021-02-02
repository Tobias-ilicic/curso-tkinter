from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()

#abre el explorador para subir un archivo del tipo que especifiquemos


def open():
    global imagen
    root.filename = filedialog.askopenfilename(initialdir = "/",title = "select a file", filetypes=(("jpg files","*.jpg"),("all files", "*.*")))
    imagen = ImageTk.PhotoImage(Image.open(root.filename))
    imagen2 = Label(root,image = imagen).pack()

boton = Button(root,text= "Seleccionar archivo", command=open).pack()

root.mainloop()