import sys
from tkinter import *
import time

def tick():
    time_string = time.strftime(" Rogan Times \n %Y-%m-%d %p %H:%M:%S ")
    clock.config(text=time_string)
    clock.after(200,tick)

root = Tk()
clock = Label(root, font = ("arial black", 60 , "italic"), bg = "grey")
clock.grid(row = 0, column = 1)
tick()
root.mainloop()
