from tkinter import Tk
from tkinter import Label
import time

c = Tk()
c.title("DIGITAL CLOCK")


def display():
    tm = time.strftime("%H:%M:%S %p ")
    lab.config(text=tm)
    lab.after(1000, display)


lab = Label(c, font=('Arial', 100), bg='black', fg='white')
lab.pack()

display()
c.mainloop()
