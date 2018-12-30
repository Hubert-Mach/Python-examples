import tkinter as tk
from tkinter import *
'''
Create multiple buttons

Documentation on buttons: http://effbot.org/tkinterbook/button.htm


Some of possible cursor options:
- arrow
- circle
- clock
- cross
- dotbox
- exchange
- fleur
- heart
- heart
- man
- mouse
- pirate
- plus
- shuttle
- sizing
- spider
- spraycan
- star
- target
- tcross
- trek
- watch
- hand2
'''


root = tk.Tk()
root.geometry("500x500")

    
arrow = Button(root, text="arrow", cursor="arrow")
arrow.pack()

circle = Button(root, text="circle", cursor="circle")
circle.pack()

clock = Button(root, text="clock", cursor="clock")
clock.pack()

cross = Button(root, text="cross", cursor="cross")
cross.pack()

dotbox = Button(root, text="dotbox", cursor="dotbox")
dotbox.pack()

exchange = Button(root, text="exchange", cursor="exchange")
exchange.pack()

fleur = Button(root, text="fleur", cursor="fleur")
fleur.pack()

heart = Button(root, text="heart", cursor="heart")
heart.pack()

hand2 = Button(root, text="hand2", cursor="hand2")
hand2.pack()



root.mainloop()