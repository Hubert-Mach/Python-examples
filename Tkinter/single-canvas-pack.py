import tkinter as tk

'''
Create canvas

Width 200 pixels
Height 200 pixels
Background black
Use pack as pack manager

Documentation on 
canvas: http://effbot.org/tkinterbook/canvas.htm
pack: http://effbot.org/tkinterbook/pack.htm
'''

root = tk.Tk()
root.geometry("500x500")

canvas_black = tk.Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="black")
canvas_black.pack()

root.mainloop()