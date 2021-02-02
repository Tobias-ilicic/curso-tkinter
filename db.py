from tkinter import *
import sqlite3
root = Tk()


#crear una base de datos para conectarla
conn = sqlite3.connect("address_book.db")

#creamos el cursor
c = conn.cursor()

#creamos una tabla
'''
la comentamos porque no la queremos crear de nuevo
c.execute("""CREATE TABLE addresses(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
)""")
'''
#Funciones
def submit():
        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()
        c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
                {
                    'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state': state.get(),
                    'zipcode': zipcode.get()
                })
        conn.commit()
        conn.close()
        #Clear the text boxes
        f_name.delete(0,END)
        l_name.delete(0,END)
        address.delete(0,END)
        city.delete(0,END)
        state.delete(0,END)
        zipcode.delete(0,END)

#funcion query
def query():
        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()

        #query la base de datos
        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()
        print(records)
        #loop por los resultados
        print_records = ""
        for record in records:
                print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + "\t" + str(record[6]) + "\n"
        
        query_label = Label(root, text=print_records)
        query_label.grid(row=12,column=0,columnspan =2)
        conn.commit()
        conn.close()
        return

#Funcion para borrar objetos de la base de datos
def delete():
        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()
        c.execute("DELETE FROM addresses WHERE oid =" + entry_delete.get())
        conn.commit()
        conn.close()

#funcion para actualizar registros
def save():
        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()
        record_id = entry_delete.get()
        c.execute('''UPDATE addresses SET 
                first_name = :first,
                last_name = :last,
                address = :address,
                city = :city,
                state = :state,
                zipcode = :zipcode

                WHERE oid = :oid''',
                {
                    'first': f_name_edit.get(),
                    'last': l_name_edit.get(),
                    'address': address_edit.get(),
                    'city': city_edit.get(),
                    'state': state_edit.get(),
                    'zipcode': zipcode_edit.get(),

                    'oid' : record_id
                })


        conn.commit()
        conn.close()
        edit_window.destroy()


def edit():
        global edit_window
        edit_window = Toplevel()
        edit_window.title("actualizar registro")

        conn = sqlite3.connect("address_book.db")
        c = conn.cursor()
        record_id = entry_delete.get()
        #query la base de datos
        c.execute("SELECT * FROM addresses WHERE oid=" + record_id)
        records = c.fetchall()
        #las convertimos en variables globales para poder usarlas
        global f_name_edit
        global l_name_edit
        global address_edit
        global city_edit
        global state_edit
        global zipcode_edit

        f_name_edit = Entry(edit_window,width = 30)
        f_name_edit.grid(row = 0, column = 1, padx = 20,pady=(10,0))
        l_name_edit = Entry(edit_window,width = 30)
        l_name_edit.grid(row = 1, column = 1, padx = 20)
        address_edit = Entry(edit_window,width = 30)
        address_edit.grid(row = 2, column = 1, padx = 20)
        city_edit = Entry(edit_window,width = 30)
        city_edit.grid(row = 3, column = 1, padx = 20)
        state_edit = Entry(edit_window,width = 30)
        state_edit.grid(row = 4, column = 1, padx = 20)
        zipcode_edit = Entry(edit_window,width = 30)
        zipcode_edit.grid(row = 5, column = 1, padx = 20)

        #titulos de las cajas
        f_name_label_edit = Label(edit_window, text = "First name")
        f_name_label_edit.grid(row = 0, column = 0,pady=(10,0))
        l_name_label_edit = Label(edit_window, text = "Last name")
        l_name_label_edit.grid(row = 1, column = 0)
        address_name_label_edit = Label(edit_window, text = "Address")
        address_name_label_edit.grid(row = 2, column = 0)
        city_name_label_edit = Label(edit_window, text = "city")
        city_name_label_edit.grid(row = 3, column = 0)
        state_name_label_edit = Label(edit_window, text = "state")
        state_name_label_edit.grid(row = 4, column = 0)
        zipcode_name_label_edit = Label(edit_window, text = "zipcode")
        zipcode_name_label_edit.grid(row = 5, column = 0)

        #loop por los resultados
        for record in records:
                f_name_edit.insert(0,record[0])
                l_name_edit.insert(0,record[1])
                address_edit.insert(0,record[2])
                city_edit.insert(0,record[3])
                state_edit.insert(0,record[4])
                zipcode_edit.insert(0,record[5])
        
        #Boton guardar
        save_btn = Button(edit_window,text="Save record", command = save)
        save_btn.grid(row = 6, column = 0, columnspan = 2, pady = 10, padx= 10,ipadx= 135)

#hacemos las text boxes
f_name = Entry(root,width = 30)
f_name.grid(row = 0, column = 1, padx = 20,pady=(10,0))
l_name = Entry(root,width = 30)
l_name.grid(row = 1, column = 1, padx = 20)
address = Entry(root,width = 30)
address.grid(row = 2, column = 1, padx = 20)
city = Entry(root,width = 30)
city.grid(row = 3, column = 1, padx = 20)
state = Entry(root,width = 30)
state.grid(row = 4, column = 1, padx = 20)
zipcode = Entry(root,width = 30)
zipcode.grid(row = 5, column = 1, padx = 20)
entry_delete = Entry(root,width = 30)
entry_delete.grid(row = 9,column = 1)

#titulos de las cajas
f_name_label = Label(root, text = "First name")
f_name_label.grid(row = 0, column = 0,pady=(10,0))
l_name_label = Label(root, text = "Last name")
l_name_label.grid(row = 1, column = 0)
address_name_label = Label(root, text = "Address")
address_name_label.grid(row = 2, column = 0)
city_name_label = Label(root, text = "city")
city_name_label.grid(row = 3, column = 0)
state_name_label = Label(root, text = "state")
state_name_label.grid(row = 4, column = 0)
zipcode_name_label = Label(root, text = "zipcode")
zipcode_name_label.grid(row = 5, column = 0)
entry_delete_label = Label(root,text = "ID number")
entry_delete_label.grid(row = 9,column = 0)
 
#hacemos el submit boton
submit_btn = Button(root, text = "add record to database",command = submit)
submit_btn.grid(row = 6,column = 0, columnspan = 2, pady = 10, padx = 10, ipadx= 100)

#creamos un boton Query
query_btn = Button(root,text="Mostrar Registros", command = query)
query_btn.grid(row = 7, column = 0, columnspan = 2, pady = 10, padx= 10,ipadx= 115)

#Boton borrar
delete_btn = Button(root,text="Delete record", command = delete)
delete_btn.grid(row = 10, column = 0, columnspan = 2, pady = 10, padx= 10,ipadx= 127)

#creamos un boton para actualizar registros
edit_btn = Button(root,text="Edit record", command = edit)
edit_btn.grid(row = 11, column = 0, columnspan = 2, pady = 10, padx= 10,ipadx= 135)

#commiteamos los cambios
conn.commit()

#cerramos la conexion con la base de datos
conn.close()

root.mainloop()