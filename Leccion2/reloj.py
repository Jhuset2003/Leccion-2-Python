#Elaborado por Albert Quintanilla y James Cadena
from tkinter import * 
import time

RelojDigital = Tk() 
RelojDigital.title("Reloj") 
RelojDigital.geometry("486x300") 



label = Label(RelojDigital, font=("Arial", 58, 'bold'), bg="Black", fg="White", bd=25)
label.grid(row=0, column=1)

label_day = Label(RelojDigital, font=("Arial", 40, 'bold'), fg="Black", bd=25)
label_day.grid(row=2, column=1)


def Reloj(): 
   tiempo = time.strftime("%I:%M:%S %p")
   dia = time.strftime("%A")
   label_day.config(text=dia)
   label.config(text=tiempo) 
   label.after(200, Reloj)


Reloj()
RelojDigital.mainloop()
