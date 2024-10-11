from tkinter import *

window = Tk()
window.title("Canvas Example")
window.minsize(width=300, height=200)
window.config(bg='lightgrey')

canvas = Canvas(window, bg='lightcyan', height=100, width=300)
canvas.pack(pady=20)

window.mainloop()

"""
    Creates a Canvas for drawing shapes or displaying images.
    
    Output: A window with a blank canvas where shapes can be drawn 
    and images can be displayed.
    
"""