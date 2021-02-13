from tkinter import *
from tkinter.ttk import *

from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, time) #every second there is a call to the time function to update time.

root = Tk()
root.title("CLOCK")

label = Label(root, font=('TkDefaultFont',80), foreground = "cyan")
label.pack(anchor = 'center')
time()
mainloop()
