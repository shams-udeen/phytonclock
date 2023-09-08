from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Ankur Gajurel Clockitty clocke")

def time():
    string = strftime('%H:%M:%S: %p')
    emma.config(text=string)
    emma.after(1000, time)

emma = Label(root , font=("ds-digital", 160), background="white", foreground="red")
emma.pack(anchor='center')
time()
mainloop()