import tkinter as tk
from tkinter import *
'''
Create multiple Labels

Documentation on Labels: http://effbot.org/tkinterbook/label.htm

IMPORTANT
Added relief to viaualize text anchor in relation to label
'''

root = tk.Tk()
root.geometry("500x500")


# As anchor following can be used: N, NE, E, SE, S, SW, W, NW, CENTER
# CENTER is default
n = Label(root, text="N anchored text Label", width=25, height=2, anchor=N, relief="groove")
n.pack()

ne = Label(root, text="NE anchored text Label", width=25, height=2, anchor=NE, relief="groove")
ne.pack()

e = Label(root, text="E anchored text Label", width=25, height=2, anchor=E, relief="groove")
e.pack()

se = Label(root, text="SE anchored text Label", width=25, height=2, anchor=SE, relief="groove")
se.pack()

s = Label(root, text="S anchored text Label", width=25, height=2, anchor=S, relief="groove")
s.pack()

sw = Label(root, text="SW anchored text Label", width=25, height=2, anchor=SW, relief="groove")
sw.pack()

w = Label(root, text="W anchored text Label", width=25, height=2, anchor=W, relief="groove")
w.pack()

nw = Label(root, text="NW anchored text Label", width=25, height=2, anchor=NW, relief="groove")
nw.pack()

center = Label(root, text="CENTER anchored text Label", width=25, height=2, anchor=CENTER, relief="groove")
center.pack()

default = Label(root, text="Default anchored text Label", width=25, height=2, relief="groove")
default.pack()


root.mainloop()