from tkinter import * 
from PIL import ImageTk, Image


root = Tk()
root.iconbitmap()
boton = Button(root, text="exit", command=root.quit).grid(row = 1,column=1)
siguiente = Button(root,text = ">>").grid(row = 1,column = 2)
previo = Button(root,text = "<<").grid(row = 1,column = 0)

status = Label(root,text = "1 of 5",bd=1,relief=SUNKEN).grid(row = 2,column = 0,columnspan = 3,sticky= W+E)


img = ImageTk.PhotoImage(Image.open("imagenes/galgo_p.jpg"))
myLabel = Label(image = img)
myLabel.grid(row=0,column=0, columnspan = 3)


root.mainloop()