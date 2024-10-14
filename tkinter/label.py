from tkinter import *

window = Tk()
window.title("Label Example")
window.minsize(width=300, height=100)
window.config(bg='lightgrey')

label = Label(window, text="This is a Label", bg='lightblue', height=2, width=20)
label.pack(pady=20)

window.mainloop()

"""
    Creates a Label widget that displays static text.
    The height and width can be adjusted accordingly.
    
    Output: A window with a label showing 'This is a Label' 
    in a light blue background.

"""