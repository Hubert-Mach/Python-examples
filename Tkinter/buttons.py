import tkinter as tk
from tkinter import *
'''
Create multiple buttons

Documentation on buttons: http://effbot.org/tkinterbook/button.htm
'''

root = tk.Tk()
root.geometry("500x500")

def callback():
    print("click!")
    
def callback2(param1, param2):
    print("Param1 is: "+str(param1)+ " param2 is: "+str(param2))
    
def quit():
    sys.exit(0)

default = Button(root, text="Default state button")
default.pack()
    
active = Button(root, text="Active button", state=ACTIVE)
active.pack()

active2 = Button(root, text="Button with function attached", command=callback)
active2.pack()

# this is needed only for creating callback with multiple parameters
from functools import partial

callparams = partial(callback2, "ONE","TWO")
active3 = Button(root, text="Button with function taking two parameters", command=callparams)
active3.pack()

disabled = Button(root, text="Disabled button", command=callback, state=DISABLED)
disabled.pack()

disabled_fg = Button(root, text="Disabled button with red", command=callback, state=DISABLED, disabledforeground="red")
disabled_fg.pack()


#  raised, flat, sunken, groove, ridge, solid
raised = Button(root, text="Raised button", relief="raised")
raised.pack()

flat = Button(root, text="Flat button", relief="flat")
flat.pack()

sunken = Button(root, text="Sunken button", relief="sunken")
sunken.pack()

groove = Button(root, text="Groove button", relief="groove")
groove.pack()

ridge = Button(root, text="Ridge button", relief="ridge")
ridge.pack()

solid = Button(root, text="Solid button", relief="solid")
solid.pack()

# Underline index starts with zero. Second character will be 1, and so on.
border = Button(root, text="Increased border button", borderwidth=8)
border.pack()

red_bg = Button(root, text="Red background button", bg = "red")
red_bg.pack()

red_fg = Button(root, text="Red foreground/text button", fg = "red")
red_fg.pack()

# Uses defined quit function as callback
quit_button = Button(root, text="Button closing program", command=quit)
quit_button.pack()


root.mainloop()