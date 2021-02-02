from tkinter import *
from PIL import ImageTk, Image
import interfaz-principal.py


root = Tk()
root.title("InstaScrap")
root.iconbitmap("C:/Users/tobi/Desktop/Proyectos/tkinter/imagenes/instagram1.ico")

def abrir():
    #si algo de aca no aparece lo tengo que definir como variable global
    nuevaVentana = Toplevel()
    label = Label(nuevaVentana, text = "que onda carnal").pack()
    nuevaVentana.title("lal")


boton = Button(root,text = "con este boton abrimos la otra ventana", command = abrir).pack()



root.mainloop()