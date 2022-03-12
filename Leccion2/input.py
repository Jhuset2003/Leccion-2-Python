from cgitb import text
from tkinter import *

root = Tk()

root.title("Mi segunda interfaz")
root.geometry("400x500")


input = Entry(root, width=60)
input.insert(0,"Ingrese un texto:")
input.pack()



def click():
    texto = input.get()
    label.configure(text=texto)
    input.delete(0,END)


button = Button(root, text="Pulsame", command=click)
button.pack()

label = Label(root, text="Soy una etiqueta")
label.pack()


root.mainloop()