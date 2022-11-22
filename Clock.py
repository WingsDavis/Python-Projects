from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime("%H:%M:%S WING$" )
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("chiller", 50), background = "black", foreground = "white")
label.pack(anchor="center")
time()

mainloop()


