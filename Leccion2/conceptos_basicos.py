from cProfile import label
from tkinter import *

root = Tk()

root.title("Mi primera interfaz")
root.geometry("400x600")

label = Label(root,text="Soy una etiqueta")
label2 = Label(root,text="Soy una etiqueta dos")

#label.pack()
#label2.pack()

label.grid(row=2 ,column=1)
label2.grid(row=10 ,column=10)
root.mainloop()