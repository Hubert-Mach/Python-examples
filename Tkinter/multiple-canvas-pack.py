import tkinter as tk

'''
Create 4 canvas

Width 200 pixels
Height 200 pixels
Background black, blue, green, red

Documentation for grid(): http://effbot.org/tkinterbook/pack.htm

'''

root = tk.Tk()
root.geometry("500x500")

canvas_black = tk.Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="black")
canvas_black.pack()

canvas_blue = tk.Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="blue")
canvas_blue.pack()

canvas_green = tk.Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="green")
canvas_green.pack()

canvas_red = tk.Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="red")
canvas_red.pack()

root.mainloop()