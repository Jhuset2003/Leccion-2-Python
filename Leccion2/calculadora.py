from tkinter import *
from turtle import width

root = Tk()

root.title("Calculadora")
frame = Frame(root, pady=3,padx=12)
frame.grid(column=0,row=1)

frame2 = Frame(root, pady=3,padx=12)
frame2.grid(column=0,row=0 )


equiation = StringVar()
calc_input = Entry(frame2, text=equiation).grid(column=0, row=1)

def press (num):
    equiation.set(equiation.get()+ str(num))

def equal_press ():
    try:
        total = eval(equiation.get())
        equiation.set(total)
    except:
        equiation.set("Math Error")


def punto():
    press(".")
def cero():
    press(0)
def uno():
    press(1)
def dos():
    press(2)
def tres():
    press(3)
def cuatro():
    press(4)
def cinco():
    press(5)
def seis():
    press(6)
def siete():
    press(7)
def ocho():
    press(8)
def nueve():
    press(9)
def suma():
    press("+")
def resta():
    press("-")
def multi():
    press("*")
def divi():
    press("/")
def clear():
    equiation.set("")
#Procesos

    

#Buttons
Button(frame,width=3, text=".",command=punto,fg="#fff", background="#666",).grid(column=2,row=5)
Button(frame,width=3, text="0",command=cero,fg="#fff", background="#666",).grid(column=1,row=5)
Button(frame,width=3, text="1",command=uno,fg="#fff", background="#666",).grid(column=3,row=4)
Button(frame,width=3, text="2",command=dos,fg="#fff", background="#666",).grid(column=2,row=4)
Button(frame,width=3, text="3",command=tres,fg="#fff", background="#666",).grid(column=1,row=4)
Button(frame,width=3, text="4",command=cuatro,fg="#fff", background="#666",).grid(column=1,row=3)
Button(frame,width=3, text="5",command=cinco,fg="#fff", background="#666",).grid(column=2,row=3)
Button(frame,width=3, text="6",command=seis,fg="#fff", background="#666",).grid(column=3,row=3)
Button(frame,width=3, text="7",command=siete,fg="#fff", background="#666",).grid(column=1,row=2)
Button(frame,width=3, text="8",command=ocho,fg="#fff", background="#666",).grid(column=2,row=2)
Button(frame,width=3, text="9",command=nueve,fg="#fff", background="#666",).grid(column=3,row=2)
Button(frame,width=3, text="Clear",command=clear,fg="#fff", background="#DC143C",).grid(column=3,row=5)

#Procesos
Button(frame,width=3, text="+",command=suma,background="#000000",fg="#fff").grid(column=4,row=2)
Button(frame,width=3, text="-",command=resta,background="#000000",fg="#fff").grid(column=4,row=3)
Button(frame,width=3, text="*",command=multi,background="#000000",fg="#fff").grid(column=4,row=4)
Button(frame,width=3, text="/",command=divi,background="#000000",fg="#fff").grid(column=4,row=5)
Button(frame,width=3, text="=",command=equal_press,background="#98FB98",fg="Black").grid(column=4,row=6)





root.mainloop()