from tkinter import *

window = Tk()
window.title("Spinbox Example")
window.minsize(width=300, height=100)
window.config(bg='lightgrey')

spinbox = Spinbox(window, from_=0, to=10, bg='lightgreen')
spinbox.pack(pady=20)

window.mainloop()

"""
Creates a Spinbox for selecting from a set of numeric values.
    
Output: A window with a Spinbox that allows users to select 
a number within a specified range using up/down arrows.

"""