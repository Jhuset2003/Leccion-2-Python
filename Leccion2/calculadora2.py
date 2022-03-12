from tkinter import *

root = Tk()

root.configure(background="Black")
root.title("Calculadora2")
root.geometry("400x200")

equiation = StringVar()
def press (num):
    equiation.set(equiation.get()+ str(num))

def equal_press ():
    try:
        total = eval(equiation.get())
        equiation.set(total)
    except:
        equiation.set("Math Error")

def clickClearly ():
    equiation.set("")
    
expression_entry = Entry(root, text=equiation)
expression_entry.grid(row=0, columnspan=4, sticky="nswe")

btn7 = Button(root, text="7",fg="#fff", background="#666", command=lambda:press(7))
btn7.grid(row=1, column=0, sticky="nswe")

btn8 = Button(root, text="8",fg="#fff", background="#666", command=lambda:press(8))
btn8.grid(row=1, column=1, sticky="nswe")

btn9 = Button(root, text="9",fg="#fff", background="#666", command=lambda:press(9))
btn9.grid(row=1, column=2, sticky="nswe")

btn6 = Button(root, text="6",fg="#fff", background="#666", command=lambda:press(6))
btn6.grid(row=2, column=0, sticky="nswe")

btn5 = Button(root, text="5",fg="#fff", background="#666", command=lambda:press(5))
btn5.grid(row=2, column=1, sticky="nswe")

btn4 = Button(root, text="4",fg="#fff", background="#666", command=lambda:press(4))
btn4.grid(row=2, column=2, sticky="nswe")

btn3 = Button(root, text="3",fg="#fff", background="#666", command=lambda:press(3))
btn3.grid(row=3, column=0, sticky="nswe")

btn2 = Button(root, text="2",fg="#fff", background="#666", command=lambda:press(2))
btn2.grid(row=3, column=1, sticky="nswe")

btn1 = Button(root, text="1",fg="#fff", background="#666", command=lambda:press(1))
btn1.grid(row=3, column=2, sticky="nswe")

btn0 = Button(root, text="0",fg="#fff", background="#666", command=lambda:press(0))
btn0.grid(row=4,column=0 , sticky="nswe",columnspan=2)

btnpunto = Button(root, text=".",fg="#fff", background="#666", command=lambda:press("."))
btnpunto.grid(row=4, column=2, sticky="nswe")

btncl = Button(root, text="Cl",fg="#fff", background="#999", command=clickClearly)
btncl.grid(row=5, column=2, sticky="nswe")

#btnopera

plus = Button(root, text="+",fg="#fff", background="#fe9727", command=lambda:press("+"))
plus.grid(row=1, column=3, sticky="nswe")

rest = Button(root, text="-",fg="#fff", background="#fe9727", command=lambda:press("-"))
rest.grid(row=2, column=3, sticky="nswe")

multi = Button(root, text="*",fg="#fff", background="#fe9727", command=lambda:press("*"))
multi.grid(row=3, column=3, sticky="nswe")

divi = Button(root, text="/",fg="#fff", background="#fe9727", command=lambda:press("/"))
divi.grid(row=4, column=3, sticky="nswe")

igual = Button(root, text="=",fg="#fff", background="#fe9727", command=equal_press)
igual.grid(row=5, column=3, sticky="nswe")



root.mainloop()





