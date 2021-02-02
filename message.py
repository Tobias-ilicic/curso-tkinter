from tkinter import *
from PIL import ImageTk, ImageTk
from tkinter import messagebox

root = Tk()
def popup():
    respuesta = messagebox.askokcancel("hola","chau")
    print(respuesta)
    #en el primero va el titulo del pop up y en el segundo el mensaje

#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
# el si o no, aceptar o cancelar returnea True o False(1 y 0)
boton = Button(root,text='pop up',command = popup).pack()


root.mainloop()