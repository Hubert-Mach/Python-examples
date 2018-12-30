import tkinter as tk

'''
Create canvas

Width 200 pixels
Height 200 pixels
Background black
Use place as geometry manager

Documentation on 
canvas: http://effbot.org/tkinterbook/canvas.htm
place: http://effbot.org/tkinterbook/place.htm
'''

root = tk.Tk()
root.geometry("500x500")

canvas_black = tk.Canvas(root, width=200, height=200, borderwidth=0, highlightthickness=0, bg="black")
canvas_black.place(x=100,y=100)

root.mainloop()