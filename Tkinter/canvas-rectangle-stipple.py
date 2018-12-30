import tkinter as tk
from tkinter import *

'''
Create canvas

Width 250 pixels
Height 500 pixels
Background red
Use pack as pack manager

Draws multiple rectangles

Documentation on 
canvas: http://effbot.org/tkinterbook/canvas.htm
pack: http://effbot.org/tkinterbook/pack.htm
'''

root = tk.Tk()
root.geometry("500x500")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# parameters: x, y, x', y' - witch represents top-left and botton-right corners
canvas.create_rectangle(0, 0, 250, 500, fill="red")

canvas.create_rectangle(200, 25, 300, 75, fill="green", stipple="")

canvas.create_rectangle(200, 100, 300, 150, fill="green", stipple="gray75")

canvas.create_rectangle(200, 175, 300, 225, fill="green", stipple="gray50")

canvas.create_rectangle(200, 250, 300, 300, fill="green", stipple="gray25")

canvas.create_rectangle(200, 325, 300, 375, fill="green", stipple="gray12")

root.mainloop()