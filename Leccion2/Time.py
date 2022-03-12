from tkinter import *
import time
from time import localtime,asctime

root = Tk()

root.configure(background="White")
root.title("Time")
root.geometry("600x300")

frame = Frame(root, pady=3,padx=12)
frame.grid(column=0,row=1)


root.mainloop()


print(asctime(localtime()))