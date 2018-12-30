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

multiline = Button(root, text="Multiline text button\nWith default align", width=25, height=2)
multiline.pack()

center = Button(root, text="Multiline text button\nWith center align", width=25, height=2, justify="center")
center.pack()

left = Button(root, text="Multiline text button\nWith left align", width=25, height=2, justify="left")
left.pack()

right = Button(root, text="Multiline text button\nWith right align", width=25, height=2, justify="right")
right.pack()


wrap = Button(root, text="Multiline text with wrap length set to 80 pixels", wraplength=80)
wrap.pack()


root.mainloop()