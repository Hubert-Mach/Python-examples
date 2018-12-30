import tkinter as tk
from tkinter import *
'''
Create multiple buttons

Documentation on buttons: http://effbot.org/tkinterbook/button.htm

Notice sizes for button with text - size is in text units
While for button with image in pixels
'''

root = tk.Tk()
root.geometry("500x500")

def callback():
    print("click!")
    
def callback2(param1, param2):
    print("Param1 is: "+str(param1)+ " param2 is: "+str(param2))
    
def quit():
    sys.exit(0)

text = Button(root, text="Text sized button", width=20, height=10)
text.pack()

from PIL import Image
bg_img=PhotoImage(file="button.png")
image = Button(root, width=100, height=100)
image.config(image=bg_img)
image.pack()


root.mainloop()