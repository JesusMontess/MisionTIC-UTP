from tkinter import *
from tkinter import messagebox
 
 
def Ok():
    nombre = entrada1.get()
    password = entrada2.get()
 
    if(nombre == "" and password == "") :
        messagebox.showinfo("", "Blank Not allowed")
 
 
    elif(nombre == "Admin" and password == "123"):
 
        messagebox.showinfo("","Login Success")
        ventana.destroy()
 
    else :
        messagebox.showinfo("","Incorrent Username and Password")
 
 
ventana = Tk()
ventana.title("formulario de entrada")
ventana.geometry("300x200")
global entrada1
global entrada2
 
Label(ventana, text="Usuario").place(x=10, y=10)
Label(ventana, text="Clave").place(x=10, y=40)
 
entrada1 = Entry(ventana)
entrada1.place(x=140, y=10)
 
entrada2 = Entry(ventana)
entrada2.place(x=140, y=40)
entrada2.config(show="*")
 
Button(ventana, text="entrar", command=Ok ,height = 2, width = 13).place(x=30, y=100)
 
ventana.mainloop()