import tkinter as tk
from tkinter import *
'''
Create multiple buttons

Documentation on buttons: http://effbot.org/tkinterbook/button.htm
'''

root = tk.Tk()
root.geometry("500x500")


# As anchor following can be used: N, NE, E, SE, S, SW, W, NW, CENTER
# CENTER is default
n = Button(root, text="N anchored text button", width=25, height=2, anchor=N)
n.pack()

ne = Button(root, text="NE anchored text button", width=25, height=2, anchor=NE)
ne.pack()

e = Button(root, text="E anchored text button", width=25, height=2, anchor=E)
e.pack()

se = Button(root, text="SE anchored text button", width=25, height=2, anchor=SE)
se.pack()

s = Button(root, text="S anchored text button", width=25, height=2, anchor=S)
s.pack()

sw = Button(root, text="SW anchored text button", width=25, height=2, anchor=SW)
sw.pack()

w = Button(root, text="W anchored text button", width=25, height=2, anchor=W)
w.pack()

nw = Button(root, text="NW anchored text button", width=25, height=2, anchor=NW)
nw.pack()

center = Button(root, text="CENTER anchored text button", width=25, height=2, anchor=CENTER)
center.pack()

default = Button(root, text="Default anchored text button", width=25, height=2)
default.pack()


root.mainloop()