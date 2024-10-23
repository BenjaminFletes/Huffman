from tkinter import *
from tkinter import filedialog
from tkinter import messagebox



def contador(ch):
    x = {}

    for i in ch:
        if i in x:
            x[i] += 1
        else:
            x[i] = 1
    print(x)

def abrir(entry):

    with open('libro.txt','r',encoding='utf-8') as arc:
        cont = arc.read() 
    entry.delete(0, END)
    entry.insert(0, cont)

w = Tk()
w.title("Hola")
w.geometry("600x600")

Tittle = Label(w, text="libro.txt")
Tittle.place(x=270,y=100)

Abrir_archivo = Button(w, text="Abrir",command=lambda:abrir(Archivito))
Abrir_archivo.place(x=270, y=200)
Archivito = Text(w,width=20,height=100)
Archivito.place(x=270,y=350)

w.mainloop()

palabra = input("Ingresa la palabra: ")
contador(palabra)

