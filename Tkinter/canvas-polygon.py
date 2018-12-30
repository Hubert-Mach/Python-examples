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

# parameters represent consecutive corners position (x,y)

# traingle red fill
canvas.create_polygon(50, 0, 100,100, 0, 100, fill="red")

# Width responsible for border set to 0 -> none border 
canvas.create_polygon(100, 50, 150,150, 50, 150, fill="green", width=0)

# White border
canvas.create_polygon(150, 100, 200, 200, 100, 200, fill="green", outline="white")

# White border with width 5
canvas.create_polygon(200, 150, 250, 250, 150, 250, fill="green", outline="white", width=5)

# Use of dash
canvas.create_polygon(250, 200, 300, 300, 200, 300, fill="green", outline="white", width=5, dash=[1])

# Another use of dash
canvas.create_polygon(300, 250, 350, 350, 250, 350, fill="green", outline="white", width=5, dash=[3,1,5])


root.mainloop()