#Albert Quintanilla y James Cadena

from ast import Try
from cgitb import text
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

def calcular_peso_planetario():
    if equiation2 == equiation2[0]:
        resultado_peso.set((float(equiation.get)*3.7)/9.8)
        print(resultado_peso)

calcular_peso = Tk()
calcular_peso.title("Calcula tu peso en otros planetas")

frame = Frame(calcular_peso, pady=3,padx=12)
frame.grid(column=0,row=0)

frame2 = Frame(calcular_peso, pady=3,padx=12)
frame2.grid(column=1,row=0 )

equiation = IntVar()
alc_input = Entry(frame2, text=equiation).grid(column=1,row=0)


equiation2 = IntVar()
equiation2.set(OptionList[0])


opt = OptionMenu(frame, equiation2, * OptionList)
opt.grid(column=3,row=0)

resultado_peso = IntVar()
res = Label(frame2, textvariable=resultado_peso).grid(column=1,row=3)



Button(frame2,width=10, text="Calcular",fg="White", background="#666", command=calcular_peso_planetario).grid(column=1,row=2)


calcular_peso.mainloop()