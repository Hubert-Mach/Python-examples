import tkinter as tk

'''
Create 4 canvas

Width 200 pixels
Height 200 pixels
Background black, blue, green, red
Arrange in two rows two columns

Documentation for grid(): http://effbot.org/tkinterbook/grid.htm

'''

root = tk.Tk()
root.geometry("500x500")

canvas_black = tk.Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="black")
canvas_black.grid(row=0, column=0)

canvas_blue = tk.Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="blue")
canvas_blue.grid(row=0, column=1)

canvas_green = tk.Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="green")
canvas_green.grid(row=1, column=0)

canvas_red = tk.Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="red")
canvas_red.grid(row=1, column=1)

root.mainloop()