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

# Defult parameters, red fill
canvas.create_oval(0, 0, 100, 100, fill="red")

# Width responsible for border set to 0 -> none border 
canvas.create_oval(50, 50, 150, 150, fill="green", width=0)

# White border
canvas.create_oval(100, 100, 200, 200, fill="green", outline="white")

# White border with width 5
canvas.create_oval(150, 150, 250, 250, fill="green", outline="white", width=5)

# Use of dash
canvas.create_oval(200, 200, 300, 300, fill="green", outline="white", width=5, dash=[1])

# Another use of dash
canvas.create_oval(250, 250, 350, 350, fill="green", outline="white", width=5, dash=[3,1,5])

# Elipse
canvas.create_oval(300, 300, 400, 350, fill="green")

root.mainloop()