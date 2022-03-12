from cProfile import label
from tkinter import *

root = Tk()

root.title("Conversor")
frame = Frame(root, pady=3,padx=12)
frame.grid(column=0,row=0)

def Calcular (*args):
    try:
        value = float(pies.get())
        resultado = int(0.3048 * value * 10000)/10000
        metros.set(resultado)
    except ValueError:
        metros.set("!ERROR¡")

pies = StringVar()
pies_inptu = Entry(frame, width=7, textvariable=pies)
pies_inptu.grid(column=1,row=0)

metros = StringVar()
metros.set("Ingrese un valor")
Label(frame, textvariable=metros ).grid(column=1,row=1)

Button(frame, text="Calcular", command=Calcular).grid(column=1,row=2)

Label(frame, text="Ingrese el valor en Pies: ").grid(column=0,row=0)
Label(frame, text="Es igual a: ").grid(column=0,row=1)
Label(frame, text="Metros").grid(column=2,row=1)

pies_inptu.focus()
root.bind("<Return>",Calcular)

root.mainloop()