import tkinter as tk
from tkinter import *
'''
Create multiple Labels

Documentation on Labels: http://effbot.org/tkinterbook/label.htm


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

    
arrow = Label(root, text="arrow", cursor="arrow")
arrow.pack()

circle = Label(root, text="circle", cursor="circle")
circle.pack()

clock = Label(root, text="clock", cursor="clock")
clock.pack()

cross = Label(root, text="cross", cursor="cross")
cross.pack()

dotbox = Label(root, text="dotbox", cursor="dotbox")
dotbox.pack()

exchange = Label(root, text="exchange", cursor="exchange")
exchange.pack()

fleur = Label(root, text="fleur", cursor="fleur")
fleur.pack()

heart = Label(root, text="heart", cursor="heart")
heart.pack()

hand2 = Label(root, text="hand2", cursor="hand2")
hand2.pack()



root.mainloop()