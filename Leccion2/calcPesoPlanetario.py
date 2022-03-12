#Albert Quintanilla y James Cadena

from ast import Try
from tkinter import *

OptionList = [
"Mercurio",
"Venus",
"Tierra",
"Marte",
"Jupiter",
"Saturno",
"Urano",
"Neptuno"
] 


def calcular_masa():
    equiation.set(int (equiation.get())/ 9.8)



calcular_peso = Tk()
calcular_peso.title("Calcula tu peso")

frame = Frame(calcular_peso, pady=3,padx=12)
frame.grid(column=0,row=0)

frame2 = Frame(calcular_peso, pady=3,padx=12)
frame2.grid(column=1,row=0 )

equiation = StringVar()
alc_input = Entry(frame2, text=equiation).grid(column=1,row=0)

Button(frame2,width=10, text="Calcular",fg="#fff", background="#666", command= calcular_masa).grid(column=1,row=2)

 

equiation2 = StringVar()



equiation2.set(OptionList[0])

opt = OptionMenu(frame, equiation2, *OptionList)
opt.grid(column=3,row=0)
opt.config(width=10, font=('Helvetica', 12))







calcular_peso.mainloop()