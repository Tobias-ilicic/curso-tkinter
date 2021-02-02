from tkinter import *

root = Tk()

#Funciones

def numeros(x):
    current = pantalla.get()
    pantalla.delete(0,END)
    pantalla.insert(0,str(current) + str(x))

def suma():
    x = int(pantalla.get())
    pantalla.delete(0,END)
    global primerNum
    primerNum = x
    global operacion
    operacion = "suma"

def resta():
    x = int(pantalla.get())
    pantalla.delete(0,END)
    global primerNum
    primerNum = x
    global operacion
    operacion = "resta"


def division():
    x = int(pantalla.get())
    pantalla.delete(0,END)
    global primerNum
    primerNum = x
    global operacion    
    operacion = "division"


def multiplicacion():
    x = int(pantalla.get())
    pantalla.delete(0,END)
    global primerNum
    primerNum = x
    global operacion
    operacion = "multiplicacion"


def igual():
    segundoNum = int(pantalla.get())
    pantalla.delete(0,END)
    if(operacion == "suma"):
        pantalla.insert(0, primerNum + segundoNum)
    if operacion == "resta":
        pantalla.insert(0, primerNum - segundoNum)
    if operacion == "multiplicacion":
        pantalla.insert(0, primerNum * segundoNum)
    if operacion == "division":
        pantalla.insert(0, primerNum / segundoNum)


def limpiar():
    pantalla.delete(0, END)
#Botones
#NUMEROS
cero = Button(root,text = "0", padx = 40 , pady = 20,command = lambda : numeros(0)).grid(row = 4 , column =0)
uno = Button(root,text = "1", padx = 40 , pady = 20, command = lambda : numeros(1)).grid(row = 1 , column =0)
dos = Button(root,text = "2", padx = 40 , pady = 20, command = lambda :numeros(2)).grid(row = 1 , column =1)
tres = Button(root,text = "3", padx = 40 , pady = 20, command = lambda :numeros(3)).grid(row = 1 , column =2)
cuatro = Button(root,text = "4", padx = 40 , pady = 20, command = lambda :numeros(4)).grid(row = 2 , column =0)
cinco = Button(root,text = "5", padx = 40 , pady = 20, command = lambda :numeros(5)).grid(row = 2 , column =1)
seis = Button(root,text = "6", padx = 40 , pady = 20, command = lambda :numeros(6)).grid(row = 2 , column =2)
siete = Button(root,text = "7", padx = 40 , pady = 20, command = lambda :numeros(7)).grid(row = 3 , column =0)
ocho = Button(root,text = "8", padx = 40 , pady = 20,command = lambda :numeros(8)).grid(row = 3 , column =1)
nueve = Button(root,text = "9", padx = 40 , pady = 20,command = lambda :numeros(9)).grid(row = 3 , column =2)

#Operaciones
botonSuma = Button(root,text = "+", padx = 40 , pady = 20, command = suma).grid(row= 4, column = 1)
botonResta = Button(root,text = "-", padx = 40 , pady = 20, command = resta).grid(row= 2, column = 3)
botonMultiplicacion = Button(root,text = "*", padx = 40 , pady = 20, command = multiplicacion).grid(row= 3, column = 3)
botonDivision = Button(root,text = "/", padx = 40 , pady = 20, command = division).grid(row= 1, column = 3)
botonIgual = Button(root,text = "=", padx = 40 , pady = 20,command = igual).grid(row= 4, column = 2)
botonLimpiar = Button(root,text = "Limpiar", padx = 22 , pady = 20, command = limpiar).grid(row= 4, column = 3)

#InputBox
pantalla = Entry(root, width = 30)
pantalla.grid(row= 0, columnspan = 2)


root.mainloop()
