from tkinter import *
from PIL import ImageTk, ImageTk
root = Tk()

frame= LabelFrame(root, text="this is my frame", padx=5, pady = 5)
frame.pack(padx=10,pady=10)
button = Button(frame,text="hola")
button.pack()
root.mainloop()

'''Puedo usar el grid sistem con los frame para posicionarlos en el root
y ademas puedo usar el grid system adentro del frame para posicionar
lo que quiero que vaya adentro'''