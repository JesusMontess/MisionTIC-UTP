from tkinter import *
from tkinter.ttk import *
#import tkinter
 
#Funciones
def imprimir():
    print("Hola")
    print(f"Texto es {entrada.get()}")
    area.insert(END,"Texto")
 
#Ventana
ventana = Tk()
ventana.title("Aplicación de prueba")
ventana.geometry("800x600")
 
manejador = Frame(ventana)
manejador.grid(row=4,column=3)
 
boton = Button(manejador,text="Esto es un botón",command=imprimir)
boton.grid(row=0,column=1)
 
etiqueta = Label(manejador,text="Presione aqui")
etiqueta.grid(row=0,column=0)
 
area = Text(manejador)
area.grid(row=1,column=1,columnspan=2)
 
arbol = Treeview(manejador)
arbol.grid(row=1,column=0, rowspan=3)
 
elem1 = arbol.insert("",END,text="Elemento 1")
elem2= arbol.insert("",END,text="Elemento 2")
 
elem11 = arbol.insert(elem1,END,text="Elemento 1.1")
elem12 = arbol.insert(elem2,END,text="Elemento 1.2")
 
entrada = Entry(manejador)
entrada.grid(row=4,column=0)
 
ventana.mainloop()