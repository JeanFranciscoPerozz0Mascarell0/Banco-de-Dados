from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


#Making GUI

w = Tk()
w.title('Contatos')
w.geometry('800x600')
w.configure(background="#000")
w.columnconfigure(0, weight=10)
w.columnconfigure(10, weight=20)


#Creating frames

frame_1 = Frame(w, background='#000')
frame_2 = Frame(w, background='#000')
frame_3 = Frame(w, background='#000')
frame_4 = Frame(w, background='#000')
frame_5 = Frame(w, background='#000')
frame_6 = Frame(w, background='#000')

# Titulo
t = Label(frame_1, text="Lista de contatos", background="#000", font="Verdana 30 bold", fg="#fff")
t.grid(column=0, row=0, padx=10, pady=10)

#BUTTONS
#create button
create_button = Button(frame_4, text="Novo Contato", height=3, width=20, background="#45f542")
create_button.grid(column=0, row=0, padx=4, pady=2)

#update button
update_button = Button(frame_4, text="Editar Contato", height=3, width=20, background="#eaed24")
update_button.grid(column=2, row=0, padx=4, pady=2)

# delete button
delete_button = Button(frame_4, text="Excluir Contato", height=3, width=20, background="#ed3124")
delete_button.grid(column=3, row=0, padx=4, pady=2)

#packing frames
frame_1.pack(anchor='center', side='top')
frame_2.pack(anchor='w', side='bottom')
frame_3.pack(anchor='w', side='bottom')
frame_4.pack(anchor='w', side='bottom')
frame_5.pack(anchor='w', side='bottom')
frame_6.pack(anchor='w', side='bottom')


connection = mysql.connector.connect(
    host = '127.0.0.1'
    user = 'root'
    password = ''
)




c= connection.cursor()
c.execute('SELECT COUNT (*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "contatos_jean";')


database_exists = c.fetchone()[0]

connection.close()

if database_exists > 0:
    print("O banco de dados existe! Iremos utiliza-lo!")
else:
    connection = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root'
        password = ''
    )

    c = connection.cursor()
    c.execute('CREATE DATABASE contatos;')
    connection.commit()
    
    connection = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'contatos'
    )

    c = connection.cursor()
    c.execute('CREATE TABLE contatos (id INT AUTO INCREMENT PRIMARY KEY,nome VARCHAR(255), cpf VARCHAR(255));')   
    connection.commit()
    connection.close()
    
class Aplicativo:
    def __init__(self, window):
        self.window = w
        self.window.title('Contatos')
        
        self.db = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            password = '',
            database='contatos'
        )
        
        self.table = ttk.Treeview(self.window, columns=('ID', 'Nome', 'cpf'), show='headings')
        self.table.heading('ID', text='ID')
        self.table.heading('Nome', text='Nome')
        self.table.heading('cpf', text='cpf')
    


if __name__ == '__main__':
    w.mainloop()