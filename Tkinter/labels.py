import tkinter as tk
from tkinter import *
'''
Create multiple Labels

Documentation on Labels: http://effbot.org/tkinterbook/label.htm
'''

root = tk.Tk()
root.geometry("500x500")



default = Label(root, text="Default state Label")
default.pack()
    
active = Label(root, text="Active Label", state=ACTIVE)
active.pack()

disabled = Label(root, text="Disabled Label", state=DISABLED)
disabled.pack()

#  raised, flat, sunken, groove, ridge, solid
raised = Label(root, text="Raised Label", relief="raised")
raised.pack()

flat = Label(root, text="Flat Label", relief="flat")
flat.pack()

sunken = Label(root, text="Sunken Label", relief="sunken")
sunken.pack()

groove = Label(root, text="Groove Label", relief="groove")
groove.pack()

ridge = Label(root, text="Ridge Label", relief="ridge")
ridge.pack()

solid = Label(root, text="Solid Label", relief="solid")
solid.pack()

# Underline index starts with zero. Second character will be 1, and so on.
border = Label(root, text="Increased border Label", borderwidth=8)
border.pack()

red_bg = Label(root, text="Red background Label", bg = "red")
red_bg.pack()

red_fg = Label(root, text="Red foreground/text Label", fg = "red")
red_fg.pack()

default = Label(root, text="Custom font Label", font="helvetica")
default.pack()

root.mainloop()