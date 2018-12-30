import tkinter as tk
import sys
import os

'''
Create full screen window

!!! WARNING !!!
There is no close button!
When run script must be interrupted or killed

'''

root = tk.Tk()

''' 
For Microsoft Windows system dedicated driver must be used
Following check sets this up
'''
if sys.platform == "win32":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
    
root.attributes("-fullscreen", True)

root.mainloop()